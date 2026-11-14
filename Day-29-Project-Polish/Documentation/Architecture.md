# AI Career Copilot – System Architecture

## 1. Architecture Overview

AI Career Copilot follows a modular architecture that integrates frontend, backend, AI processing, document processing, and external job data sources.

## 2. Main Components

### Frontend

- Streamlit
- Provides user interface.
- Accepts resume uploads and displays results.

### Backend

- FastAPI
- Handles API requests.
- Connects frontend with processing modules.

### AI Processing

- LangChain
- LangGraph
- RAG (Retrieval-Augmented Generation)
- Supports resume analysis, skill gap identification, and AI-generated content.

### Document Processing

- Extracts text from uploaded resumes.
- Splits text into chunks.
- Generates embeddings for semantic retrieval.

### Vector Database

- Stores document embeddings.
- Supports similarity-based retrieval.

### External Job Sources

- Adzuna API
- Arbeitnow API
- Retrieves relevant job opportunities.

## 3. System Workflow

1. User uploads a resume.
2. System extracts resume content.
3. Resume text is divided into chunks.
4. Embeddings are generated and stored.
5. Job APIs retrieve relevant opportunities.
6. AI analyzes skills and job requirements.
7. System identifies skill gaps.
8. AI generates tailored resumes and cover letters.
9. User tracks application progress.

## 4. Technologies

Python, Streamlit, FastAPI, LangChain, LangGraph, RAG, Vector Database, Adzuna API, Arbeitnow API.

## 5. Future Architecture Improvements

- Authentication and authorization.
- Scalable cloud deployment.
- Improved vector search.
- More job API integrations.
- Better monitoring and error handling.
