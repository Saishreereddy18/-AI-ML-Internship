# Day 18 – AI Agent Design Document

## 1. Project Title

AI Research Assistant Agent

## 2. Learning Objectives

- Understand AI agents and their applications.
- Learn agent planning and task execution.
- Understand tool usage and decision-making.
- Design an agent workflow.
- Learn the ReAct approach.

## 3. Objective

The objective of the AI Research Assistant Agent is to help employees find information from company documents quickly and accurately. It retrieves relevant information, analyzes the results, and generates answers based on the available documents.

## 4. Problem Statement

Employees often spend considerable time searching through company policies, reports, and technical documents. Manually finding the correct information can be time-consuming. An AI Research Assistant Agent simplifies this process by searching documents and providing relevant answers.

## 5. Available Tools

1. **Python:** Executes the agent's processing logic.
2. **Document Retriever:** Searches for relevant document sections.
3. **Embedding Model:** Converts text into numerical vectors for semantic search.
4. **ChromaDB / FAISS:** Stores and retrieves document embeddings.
5. **Large Language Model (LLM):** Generates answers from retrieved information.
6. **RAG Pipeline:** Connects document retrieval with answer generation.

## 6. Agent Planning

The agent follows these steps:

1. Receive the user's question.
2. Analyze the question and identify the required information.
3. Select the appropriate retrieval tool.
4. Search the company document knowledge base.
5. Check whether the retrieved information is relevant.
6. If information is insufficient, refine the search or ask for clarification.
7. Generate an answer based on the retrieved evidence.
8. Return the answer with source references when available.

## 7. Decision-Making Process

The agent selects its next action based on the question and search results.

- If relevant information is found, generate an answer.
- If information is incomplete, perform another search.
- If the question is unclear, ask the user to clarify.
- If information is unavailable, inform the user rather than inventing an answer.

## 8. ReAct Approach

ReAct stands for Reasoning and Acting. It combines reasoning, actions, and observations to complete a task.

Example:

- **Question:** How many work-from-home days are allowed per week?
- **Plan:** Find the company's work-from-home policy.
- **Action:** Search the document database.
- **Observation:** Review the relevant policy section retrieved by the search tool.
- **Decision:** Check whether the retrieved section answers the question.
- **Final Answer:** State the allowance specified in the policy, with a source reference when available.

## 9. Expected Outputs

- Relevant answers to employee questions.
- Retrieved document sections.
- Source references when available.
- Clarification requests for ambiguous questions.
- An appropriate message when information cannot be found.

## 10. Benefits

- Reduces manual document searching.
- Improves employee productivity.
- Provides faster access to company information.
- Supports evidence-based answers.
- Can be extended with additional tools and data sources.

## 11. Conclusion

The AI Research Assistant Agent demonstrates how AI agents use planning, tool selection, retrieval, and language generation to solve practical business problems. It can be integrated with a Retrieval-Augmented Generation (RAG) pipeline to provide useful answers from company documents.
