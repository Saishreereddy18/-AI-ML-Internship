# Day 18 – Use Case Description

## 1. Use Case Title

AI Research Assistant for Company Documents

## 2. Overview

The AI Research Assistant Agent helps employees search company documents and obtain relevant answers without manually reading multiple files.

## 3. Problem Statement

Employees may need to search through company policies, reports, and technical documentation to find specific information. Manual searching takes time and can make information difficult to locate.

The proposed AI agent uses document retrieval and language generation to simplify this process.

## 4. Primary Actor

**Company Employee:** The employee asks questions and receives information from the company's document knowledge base.

## 5. Supporting Components

- AI Agent Controller
- Document Retriever
- Embedding Model
- Vector Database (ChromaDB or FAISS)
- Large Language Model (LLM)
- Company Document Repository

## 6. Preconditions

- Company documents are available to the system.
- Documents have been processed and indexed for retrieval.
- The retrieval and answer-generation components are configured.
- The employee has permission to access the requested information.

## 7. Main Flow

1. The employee enters a question.
2. The agent analyzes the question.
3. The agent selects the document retrieval tool.
4. The retrieval tool searches the indexed company documents.
5. The agent evaluates the retrieved information.
6. The LLM generates an answer using the relevant content.
7. The system displays the answer and source references when available.

## 8. Alternative Flow

- If the search results are incomplete, the agent refines the search.
- If the question is ambiguous, the agent asks for clarification.
- If no relevant information is found, the agent informs the employee.
- If the user lacks permission, the system does not disclose restricted information.

## 9. Example Scenario

**User Question:** How many work-from-home days are allowed per week?

**Agent Action:** Searches the company's work-from-home policy and retrieves the relevant section.

**Expected Response:** The agent provides the allowance specified in the retrieved policy and identifies the source document when available.

The agent must not invent a policy answer if the relevant information cannot be found.

## 10. Expected Outcome

- Faster access to company information.
- Reduced manual document searching.
- Clear answers grounded in available documents.
- Better employee productivity.
- Improved traceability through source references.

## 11. Conclusion

The AI Research Assistant Agent provides a practical way to access company information using AI-based retrieval and language generation. It demonstrates agent planning, tool usage, decision-making, and the ReAct workflow.
