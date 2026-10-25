# Day 16 – Basic RAG Pipeline and Retrieval Performance Analysis

## Project Overview

This project implements a basic Retrieval-Augmented Generation (RAG) pipeline using company documentation. It allows users to ask questions about company policies and retrieves relevant information using text embeddings, semantic search, and vector databases.

The project also compares different document chunk sizes to analyze their impact on retrieval performance.

## Learning Objectives

- Understand text embeddings and semantic search.
- Learn how vector databases work.
- Implement document retrieval using ChromaDB and FAISS.
- Build a basic RAG pipeline.
- Experiment with different document chunk sizes.
- Evaluate retrieval performance and compare results.

## Technologies Used

- Python
- Jupyter Notebook
- Pandas and NumPy
- Sentence Transformers
- Scikit-learn
- ChromaDB
- FAISS
- Matplotlib

## Project Structure

```text
Day-16-RAG-Pipeline-and-Retrieval-Analysis/
│
├── RAG_Pipeline.ipynb
├── company_documentation.txt
├── response_evaluation.csv
├── chunk_size_comparison.csv
├── Comparison_Report.md
├── README.md
└── requirements.txt
```

## Project Workflow

1. **Document Loading:** Load company documentation containing company policies and employee information.
2. **Document Chunking:** Divide documents into smaller text sections to improve retrieval.
3. **Embedding Generation:** Convert document chunks into numerical vectors using Sentence Transformers.
4. **Vector Storage:** Store embeddings and documents in ChromaDB and create a FAISS similarity-search index.
5. **Semantic Search:** Retrieve relevant document chunks based on the meaning of the user's question.
6. **Answer Generation:** Use retrieved context to produce an answer. The initial implementation uses an extractive answer baseline.
7. **Performance Evaluation:** Compare retrieval results across different chunk sizes.

## Practical Implementation

The system uses sample company documentation covering:

- Company working hours
- Paid leave policy
- Work-from-home policy
- IT support information
- Security policies
- Expense reimbursement
- Employee performance reviews
- New employee onboarding

Example question:

**Question:** How many paid leaves do employees receive?

**Expected answer:** Employees receive 18 paid leaves per calendar year.

## Chunk Size Experiment

The project evaluates three document chunk sizes:

| Chunk Size       | Description                                 |
| ---------------- | ------------------------------------------- |
| 200 characters   | Smaller, more focused text chunks           |
| 500 characters   | Medium-sized chunks                         |
| 1,000 characters | Larger chunks with more surrounding context |

The evaluation checks whether expected information appears in the top three retrieved chunks for each test question.

The best-performing chunk size is identified using the measured retrieval accuracy. Actual results are recorded in `chunk_size_comparison.csv` and discussed in `Comparison_Report.md`.

## Evaluation Metrics

- Retrieval correctness
- Number of correctly retrieved answers
- Total evaluation questions
- Retrieval accuracy percentage

**Retrieval Accuracy:**

Retrieval Accuracy (%) = (Correctly Retrieved Answers / Total Questions) × 100

The current evaluation uses an exact expected-text match. This is a baseline metric and may not recognize semantically correct answers expressed using different wording.

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Saishreereddy18/-AI-ML-Internship.git
```

### 2. Navigate to the project folder

```bash
cd -AI-ML-Internship/Day-16-RAG-Pipeline-and-Retrieval-Analysis
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start Jupyter Notebook

```bash
jupyter notebook
```

Open `RAG_Pipeline.ipynb` and run the cells in order.

The embedding model may need to be downloaded the first time it is used. An internet connection may be required.

## Results and Findings

The chunk-size experiment demonstrates how document segmentation can affect semantic retrieval. Smaller chunks may provide more precise information, while larger chunks may preserve additional context.

The final conclusion should be based on the actual retrieval accuracy recorded by the notebook rather than assuming a particular chunk size will always perform best.

## Limitations

- The initial answer-generation implementation is extractive rather than a generative LLM.
- Evaluation uses a small set of sample company-policy questions.
- Exact-text matching does not fully measure semantic correctness.
- Performance may vary with the embedding model, chunk overlap, document structure, and evaluation dataset.

## Future Improvements

- Integrate a generative LLM for context-grounded answers.
- Add semantic answer evaluation and faithfulness checks.
- Expand the company documentation and evaluation dataset.
- Compare ChromaDB and FAISS retrieval performance.
- Develop a Streamlit interface for interactive company-policy question answering.

## Conclusion

This project demonstrates the fundamentals of Retrieval-Augmented Generation, including document processing, embeddings, vector search, and retrieval evaluation. The chunk-size experiment provides a baseline for understanding how document segmentation affects retrieval performance.

**Project:** Day 16 – Basic RAG Pipeline and Retrieval Performance Analysis  
**Internship:** Linkific AIML Internship  
**Author:** Billa Sai Sree
