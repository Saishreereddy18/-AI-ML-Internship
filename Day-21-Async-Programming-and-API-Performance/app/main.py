
from fastapi import (
    FastAPI, UploadFile, File, HTTPException,
    BackgroundTasks, Depends, Request
)
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from pypdf import PdfReader
from pathlib import Path
from io import BytesIO
from starlette.concurrency import run_in_threadpool
import hashlib
import re
import asyncio
import logging
import time

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Day 21 - Async RAG API",
    description="Asynchronous PDF upload and question-answering API",
    version="2.0.0"
)

# Configuration
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
MAX_FILE_SIZE = 10 * 1024 * 1024

# In-memory document store
documents = {}


# ---------------- DEPENDENCY INJECTION ----------------

def get_document_store():
    return documents


# ---------------- REQUEST VALIDATION ----------------

class QuestionRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        max_length=1000,
        description="Question about the uploaded PDF"
    )


# ---------------- PDF PROCESSING ----------------

def extract_pdf_text(file_bytes: bytes):
    """Extract PDF text and page count."""
    try:
        reader = PdfReader(BytesIO(file_bytes))

        if reader.is_encrypted:
            if not reader.decrypt(""):
                raise ValueError("Password-protected PDFs are not supported.")

        pages = [
            page.extract_text() or ""
            for page in reader.pages
        ]

        text = "\n".join(pages).strip()

        if not text:
            raise ValueError("PDF contains no extractable text.")

        return text, len(reader.pages)

    except ValueError:
        raise
    except Exception as exc:
        raise ValueError("Invalid or unreadable PDF file.") from exc


def create_chunks(text: str):
    """Split text into overlapping chunks."""
    chunks = []
    start = 0

    while start < len(text):
        end = min(start + CHUNK_SIZE, len(text))
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end == len(text):
            break

        start = end - CHUNK_OVERLAP

    return chunks


def retrieve_relevant_chunks(question: str, chunks: list, top_k=3):
    """Keyword-based document retrieval."""
    question_words = set(re.findall(r"\b\w+\b", question.lower()))

    stop_words = {
        "what", "is", "are", "the", "a", "an", "of",
        "to", "in", "on", "for", "how", "does", "do",
        "can", "i", "we", "you", "and", "or", "with"
    }

    question_words -= stop_words
    scored_chunks = []

    for chunk in chunks:
        chunk_words = set(re.findall(r"\b\w+\b", chunk.lower()))
        score = len(question_words & chunk_words)

        if score:
            scored_chunks.append((score, chunk))

    scored_chunks.sort(key=lambda item: item[0], reverse=True)

    return [chunk for score, chunk in scored_chunks[:top_k]]


# ---------------- BACKGROUND TASK ----------------

def log_upload(document_id: str, filename: str):
    """Log successful upload after returning the response."""
    logger.info(
        "Background task: Document %s (%s) uploaded.",
        document_id,
        filename
    )


# ---------------- MIDDLEWARE ----------------

@app.middleware("http")
async def performance_middleware(request: Request, call_next):
    """Measure API response time."""
    start_time = time.perf_counter()

    response = await call_next(request)

    elapsed_time = time.perf_counter() - start_time

    response.headers["X-Process-Time"] = f"{elapsed_time:.6f}"

    logger.info(
        "%s %s completed in %.4f seconds",
        request.method,
        request.url.path,
        elapsed_time
    )

    return response


# ---------------- API ENDPOINTS ----------------

@app.get("/")
async def home():
    return {
        "message": "Welcome to Async RAG API",
        "version": "2.0.0",
        "docs": "/docs",
        "health": "/api/v1/health"
    }


@app.get("/api/v1/health")
async def health_check(
    store: dict = Depends(get_document_store)
):
    return {
        "status": "healthy",
        "uploaded_documents": len(store),
        "api_version": "v1"
    }


@app.post("/api/v1/upload")
async def upload_document(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    store: dict = Depends(get_document_store)
):
    """Asynchronously upload and process a PDF."""

    if not file.filename:
        raise HTTPException(400, "Filename is required.")

    filename = Path(file.filename).name

    if Path(filename).suffix.lower() != ".pdf":
        raise HTTPException(415, "Only PDF files are supported.")

    file_bytes = await file.read(MAX_FILE_SIZE + 1)

    if len(file_bytes) > MAX_FILE_SIZE:
        raise HTTPException(413, "File exceeds the 10 MB size limit.")

    if not file_bytes:
        raise HTTPException(400, "Uploaded file is empty.")

    try:
        # Run CPU/file processing outside the event loop.
        text, page_count = await run_in_threadpool(
            extract_pdf_text, file_bytes
        )

        chunks = await run_in_threadpool(create_chunks, text)

    except ValueError as exc:
        raise HTTPException(400, str(exc))

    if not chunks:
        raise HTTPException(400, "No usable text chunks were created.")

    document_id = hashlib.sha256(file_bytes).hexdigest()[:12]

    metadata = {
        "document_id": document_id,
        "filename": filename,
        "page_count": page_count,
        "character_count": len(text),
        "chunk_count": len(chunks),
        "chunk_size": CHUNK_SIZE,
        "chunk_overlap": CHUNK_OVERLAP
    }

    store[document_id] = {
        "filename": filename,
        "text": text,
        "chunks": chunks,
        "metadata": metadata
    }

    # Execute logging after the response is sent.
    background_tasks.add_task(
        log_upload, document_id, filename
    )

    return {
        "message": "Document uploaded successfully.",
        **metadata
    }


@app.post("/api/v1/ask/{document_id}")
async def ask_question(
    document_id: str,
    request: QuestionRequest,
    store: dict = Depends(get_document_store)
):
    """Asynchronously retrieve relevant document information."""

    if document_id not in store:
        raise HTTPException(404, "Document not found.")

    question = request.question.strip()

    if not question:
        raise HTTPException(400, "Question cannot be empty.")

    doc = store[document_id]

    retrieved = await run_in_threadpool(
        retrieve_relevant_chunks,
        question,
        doc["chunks"]
    )

    if not retrieved:
        answer = "No relevant information was found in this document."
    else:
        answer = (
            "Relevant information from the uploaded document:\n\n"
            + "\n\n".join(retrieved)
        )

    return {
        "document_id": document_id,
        "question": question,
        "answer": answer,
        "retrieved_chunks": retrieved
    }


@app.get("/api/v1/documents")
async def list_documents(
    store: dict = Depends(get_document_store)
):
    return {
        "count": len(store),
        "documents": [
            doc["metadata"] for doc in store.values()
        ]
    }


# ---------------- ASYNC BACKGROUND TASK DEMO ----------------

async def simulated_background_job():
    """Example asynchronous background operation."""
    await asyncio.sleep(2)
    logger.info("Asynchronous background job completed.")


@app.post("/api/v1/background-demo")
async def background_demo(
    background_tasks: BackgroundTasks
):
    background_tasks.add_task(simulated_background_job)

    return {
        "message": "Background task scheduled successfully."
    }
