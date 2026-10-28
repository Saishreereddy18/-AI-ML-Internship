# Day 19 – LangGraph Workflow and Error Handling

## Project Overview

A graph-based company question-answering system built with LangGraph. It demonstrates nodes, graph edges, shared state, conditional routing, loops, memory, and error recovery.

## Features

- Question input and document retrieval
- Context-based answer generation
- Conditional routing for success, missing context, and errors
- Conversation memory
- Loop-based interaction for multiple questions
- Simulated retrieval failure and recovery

## Technologies

- Python
- LangGraph
- TypedDict
- Conditional graph routing

## How to Run

1. Install dependencies using `python -m pip install -r requirements.txt`.
2. Run `python langgraph_workflow.py`.
3. Enter a question about company policies.
4. Enter a question with `[fail]` to test error recovery.
5. Enter `exit` to stop the program.

## Deliverables

- `langgraph_workflow.py` – Working workflow
- `workflow_diagram.md` – Updated LangGraph diagram
- `workflow_analysis_report.md` – Workflow analysis
- `error_handling_notes.md` – Failure scenarios and recovery strategies

## Learning Outcome

Practised graph construction, node-based execution, state management, conditional routing, memory, loops, and error handling using LangGraph.
