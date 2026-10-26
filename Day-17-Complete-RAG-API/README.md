# Day 17 – Complete RAG API

## Project Overview

This project implements a REST API using FastAPI to upload PDF documents, extract their text, divide the text into smaller chunks, store document metadata, and retrieve relevant information based on user questions.

The project focuses on API development, PDF processing, text chunking, document retrieval, input validation, and robustness testing.

## Objectives

- Build a REST API using FastAPI.
- Upload and process PDF documents.
- Extract text from PDF files using PyPDF.
- Split extracted text into manageable chunks.
- Store document metadata for tracking.
- Retrieve relevant text chunks using keyword matching.
- Test API endpoints and error-handling scenarios through Swagger UI.

## Technologies Used

- Python
- FastAPI
- Uvicorn
- PyPDF
- Python Multipart
- Pydantic
- Swagger UI

## Features

- PDF upload with file-type validation.
- Maximum file size of 10 MB.
- PDF text extraction and chunk creation.
- Chunk size: 500 characters.
- Chunk overlap: 50 characters.
- Document metadata tracking.
- Keyword-based relevant chunk retrieval.
- Health-check endpoint.
- Document listing endpoint.
- Error handling for empty files, unsupported formats, oversized uploads, and unknown document IDs.

## Project Structure

```text
Day-17-Complete-RAG-API/
├── main.py
├── requirements.txt
├── README.md
├── testing_report.md
└── screenshots/
    ├── 01-health-check.png
    ├── 02-pdf-upload-success.png
    ├── 03-ask-question-success.png
    ├── 04-list-documents.png
    ├── 05-unsupported-file-415.png

```

## Installation and Setup

### 1. Open the project directory

```powershell
cd "C:\Users\saish\OneDrive\Desktop\AIML-Internship\Day-17-Complete-RAG-API"
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Start the FastAPI server

```powershell
python -m uvicorn main:app --reload
```

### 4. Open Swagger UI

Visit:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Use Swagger UI to execute requests, upload PDF files, ask questions, and inspect responses.

## API Endpoints

| Method | Endpoint             | Description                          |
| ------ | -------------------- | ------------------------------------ |
| GET    | `/`                  | Display the API welcome message      |
| GET    | `/health`            | Check API health                     |
| POST   | `/upload`            | Upload and process a PDF             |
| POST   | `/ask/{document_id}` | Retrieve relevant text chunks        |
| GET    | `/documents`         | List uploaded documents and metadata |

## How to Use

### 1. Upload a PDF

Send a `POST` request to `/upload` using multipart form data with a PDF file.

The API extracts text, creates chunks, and returns metadata including the document ID, page count, character count, and chunk count.

### 2. Ask a question

Send a `POST` request to `/ask/{document_id}` with a JSON request body:

```json
{
  "question": "What programming languages and technical skills are listed in the resume?"
}
```

The API identifies matching chunks using keyword overlap and returns relevant text from the uploaded document.

### 3. List documents

Send a `GET` request to `/documents` to view uploaded document metadata.

### 4. Check API health

Send a `GET` request to `/health` to verify that the API is running.

## Testing and Results

The following test cases were executed successfully:

| Test Case                   | Expected HTTP Status | Result |
| --------------------------- | -------------------: | ------ |
| Health check                |                  200 | PASS   |
| Valid PDF upload            |                  200 | PASS   |
| Relevant question retrieval |                  200 | PASS   |
| List documents              |                  200 | PASS   |
| Unsupported file format     |                  415 | PASS   |
| Empty file upload           |                  400 | PASS   |
| Unknown document ID         |                  404 | PASS   |
| File larger than 10 MB      |                  413 | PASS   |

### Sample PDF Processing Results

- Filename: `Saishree_resume.pdf`
- Pages processed: 1
- Extracted characters: 3,497
- Chunks created: 8
- Chunk size: 500 characters
- Chunk overlap: 50 characters

See the `screenshots/` folder for API test evidence and `testing_report.md` for the detailed testing report.

## Limitations

- The current retrieval method uses keyword matching rather than embedding-based semantic search.
- The API returns retrieved document text instead of generating new answers with an LLM.
- Uploaded documents are stored in application memory and are lost when the server restarts.
- Only PDFs containing extractable text are supported.
- The maximum upload size is 10 MB.

## Future Enhancements

- Integrate embedding models and semantic search.
- Add ChromaDB or FAISS for vector storage and retrieval.
- Integrate an LLM to generate answers grounded in retrieved chunks.
- Add persistent document storage.
- Support scanned PDFs using OCR.
- Implement automated tests, authentication, and logging.

## Conclusion

This project demonstrates the development and testing of a PDF-based retrieval API using FastAPI. It covers document processing, text chunking, keyword-based retrieval, metadata management, REST API design, and error handling. It provides a foundation for future development into a more advanced retrieval-augmented generation system.

---

**Project:** Day 17 – Complete RAG API
**Category:** AI/ML Internship – API Development and Retrieval Systems
