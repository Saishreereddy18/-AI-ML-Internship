
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from pypdf import PdfReader
from pathlib import Path
from io import BytesIO
import hashlib
import re

app = FastAPI(
    title="Day 17 - Complete RAG API",
    description="Upload PDF documents and ask questions about their content.",
    version="1.0.0"
)

# Configuration
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

# In-memory document store
documents = {}


class QuestionRequest(BaseModel):
    question: str


def extract_pdf_text(file_bytes: bytes) -> str:
    """Extract text from a PDF document."""
    try:
        reader = PdfReader(BytesIO(file_bytes))

        if reader.is_encrypted:
            try:
                if not reader.decrypt(""):
                    raise HTTPException(
                        status_code=400,
                        detail="Password-protected PDFs are not supported."
                    )
            except HTTPException:
                raise
            except Exception:
                raise HTTPException(
                    status_code=400,
                    detail="Unable to decrypt this PDF."
                )

        pages = []
        for page in reader.pages:
            pages.append(page.extract_text() or "")

        text = "\n".join(pages).strip()

        if not text:
            raise HTTPException(
                status_code=400,
                detail="The PDF contains no extractable text."
            )

        return text

    except HTTPException:
        raise
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid or unreadable PDF file."
        )


def create_chunks(text: str):
    """Split text into overlapping character-based chunks."""
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


def retrieve_relevant_chunks(question: str, chunks: list, top_k: int = 3):
    """Basic keyword-based retrieval baseline."""
    question_words = set(
        re.findall(r"\b\w+\b", question.lower())
    )

    stop_words = {
        "what", "is", "are", "the", "a", "an", "of",
        "to", "in", "on", "for", "how", "does", "do",
        "can", "i", "we", "you", "and", "or", "with"
    }

    question_words -= stop_words
    scored_chunks = []

    for chunk in chunks:
        chunk_words = set(
            re.findall(r"\b\w+\b", chunk.lower())
        )
        score = len(question_words & chunk_words)

        if score > 0:
            scored_chunks.append((score, chunk))

    scored_chunks.sort(key=lambda item: item[0], reverse=True)

    return [
        chunk for score, chunk in scored_chunks[:top_k]
    ]


@app.get("/")
def home():
    return {
        "message": "Welcome to the Complete RAG API",
        "docs": "/docs",
        "health": "/health"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "uploaded_documents": len(documents)
    }


@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """Upload a PDF, extract text, create chunks, and save metadata."""

    if not file.filename:
        raise HTTPException(status_code=400, detail="Filename is required.")

    if Path(file.filename).suffix.lower() != ".pdf":
        raise HTTPException(
            status_code=415,
            detail="Unsupported file format. Please upload a PDF."
        )

    file_bytes = await file.read(MAX_FILE_SIZE + 1)

    if len(file_bytes) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail="File exceeds the 10 MB size limit."
        )

    if not file_bytes:
        raise HTTPException(status_code=400, detail="Uploaded file is empty.")

    text = extract_pdf_text(file_bytes)
    chunks = create_chunks(text)

    if not chunks:
        raise HTTPException(
            status_code=400,
            detail="No usable text chunks were created."
        )

    document_id = hashlib.sha256(file_bytes).hexdigest()[:12]

    documents[document_id] = {
        "filename": Path(file.filename).name,
        "text": text,
        "chunks": chunks,
        "metadata": {
            "document_id": document_id,
            "filename": Path(file.filename).name,
            "page_count": len(PdfReader(BytesIO(file_bytes)).pages),
            "character_count": len(text),
            "chunk_count": len(chunks),
            "chunk_size": CHUNK_SIZE,
            "chunk_overlap": CHUNK_OVERLAP
        }
    }

    return {
        "message": "Document uploaded and processed successfully.",
        **documents[document_id]["metadata"]
    }


@app.post("/ask/{document_id}")
def ask_question(document_id: str, request: QuestionRequest):
    """Retrieve relevant document chunks for a user's question."""

    if document_id not in documents:
        raise HTTPException(
            status_code=404,
            detail="Document not found. Upload the PDF first."
        )

    question = request.question.strip()

    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    doc = documents[document_id]
    retrieved = retrieve_relevant_chunks(question, doc["chunks"])

    if not retrieved:
        return {
            "document_id": document_id,
            "question": question,
            "answer": "No relevant information was found in this document.",
            "retrieved_chunks": []
        }

    # This is a retrieval baseline, not an LLM-generated answer.
    return {
        "document_id": document_id,
        "question": question,
        "answer": (
            "Relevant information from the uploaded document:\n\n"
            + "\n\n".join(retrieved)
        ),
        "retrieved_chunks": retrieved
    }


@app.get("/documents")
def list_documents():
    """List uploaded documents and their metadata."""
    return {
        "count": len(documents),
        "documents": [
            doc["metadata"] for doc in documents.values()
        ]
    }
