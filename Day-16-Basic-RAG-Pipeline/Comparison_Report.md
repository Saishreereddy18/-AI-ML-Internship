# Day 16 – RAG Retrieval Performance Analysis

## Objective

Build a basic RAG pipeline using company documentation,
embeddings, semantic search, and vector databases.

## Technologies

Python, Sentence Transformers, ChromaDB, FAISS,
Pandas, NumPy, Matplotlib, Jupyter Notebook.

## Experiment

Chunk sizes tested: 200, 500, and 1000 characters.
Evaluation questions: 8
Retrieval metric: expected information found in top 3 chunks.

## Results

Chunk Size Correct_Answers Total_Questions Accuracy Accuracy (%)
200 6 8 0.75 75.0
500 6 8 0.75 75.0
1000 6 8 0.75 75.0

## Best Performing Chunk Size

The best-performing tested chunk size was 200
characters, with retrieval accuracy of 75.00%.

## Findings

Chunk size affects how much context is retrieved.
Smaller chunks may provide focused information, while
larger chunks may preserve surrounding context.
The measured results determine which setting performed
best on this dataset and evaluation questions.

## Limitations

The current metric checks exact expected-text matches.
It does not fully measure semantic correctness or the
quality of generated answers. The current answer baseline
is extractive rather than a generative LLM.

## Conclusion

This experiment establishes a baseline for comparing
RAG retrieval performance across different chunk sizes.
