# Day 17 – Complete RAG API Testing Report

## 1. Objective

To build and test a FastAPI application that accepts PDF documents, extracts text, creates text chunks, stores document metadata, and retrieves relevant text in response to user questions.

## 2. Technologies Used

- Python
- FastAPI
- Uvicorn
- PyPDF
- Python Multipart
- Swagger UI

## 3. Features Implemented

- PDF document upload and validation
- Text extraction from PDF files
- Text chunking with a chunk size of 500 characters and 50-character overlap
- Document metadata tracking
- Keyword-based retrieval of relevant text chunks
- REST API endpoints for health checks, uploads, questions, and document listing
- Validation for empty files, unsupported formats, oversized files, and unknown document IDs

## 4. Test Results

| Test Case           | Expected Result                | Actual Result                                | Status |
| ------------------- | ------------------------------ | -------------------------------------------- | ------ |
| Health check        | API reports healthy            | HTTP 200; status healthy                     | PASS   |
| Valid PDF upload    | Extract text and create chunks | HTTP 200; 1 page, 3,497 characters, 8 chunks | PASS   |
| Relevant question   | Retrieve relevant text         | HTTP 200; relevant resume text returned      | PASS   |
| List documents      | Return document metadata       | HTTP 200; 1 document listed                  | PASS   |
| Unsupported file    | Reject non-PDF file            | HTTP 415                                     | PASS   |
| Empty file          | Reject empty upload            | HTTP 400                                     | PASS   |
| Unknown document ID | Return not found               | HTTP 404                                     | PASS   |
| Oversized file      | Reject file larger than 10 MB  | HTTP 413                                     | PASS   |

## 5. API Endpoints

- `GET /` – API welcome message
- `GET /health` – API health status
- `POST /upload` – Upload and process a PDF
- `POST /ask/{document_id}` – Retrieve relevant text for a question
- `GET /documents` – List uploaded documents and metadata

## 6. Limitations

- Retrieval uses keyword matching rather than embedding-based semantic search.
- Responses return retrieved text instead of LLM-generated answers.
- Documents are stored in memory and are lost when the server restarts.
- Only PDFs with extractable text are supported.
- Maximum upload size is 10 MB.

## 7. Future Improvements

- Integrate embeddings and vector search using ChromaDB or FAISS.
- Add an LLM to generate grounded answers from retrieved chunks.
- Persist document data in a database or vector store.
- Add OCR support for scanned PDFs.
- Add automated tests, logging, and authentication.

## 8. Conclusion

The Day 17 FastAPI application was tested successfully for document upload, text extraction, chunk creation, retrieval, metadata listing, and error handling. The project establishes a foundation for a more advanced RAG system with semantic retrieval and LLM integration.
