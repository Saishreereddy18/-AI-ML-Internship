# Day 19 – LangGraph Workflow Analysis Report

## 1. Project Title

Company Question Answering System Using LangGraph

## 2. Objective

To design a graph-based question-answering workflow using nodes, edges, shared state, conditional routing, loops, and memory.

## 3. Workflow Overview

The workflow receives a user's question, retrieves relevant company documents, generates an answer from the retrieved context, and saves the question-answer pair in memory.

## 4. Nodes Used

1. **Receive Question:** Accepts the user's question and initializes workflow state.
2. **Retrieve Documents:** Searches the local company-document collection.
3. **Generate Answer:** Formats the retrieved information into an answer.
4. **No Context Response:** Handles questions without relevant document matches.
5. **Error Recovery:** Handles a simulated retrieval failure and provides a retry message.
6. **Save Memory:** Stores the question-answer pair in the conversation's in-memory list.

## 5. State Management

The shared state contains the question, retrieved documents, context, answer, memory, and error information. Each node reads the information it needs and returns state updates for the next node.

## 6. Conditional Routing

After retrieval, the workflow checks the result:

- If relevant documents are found, it routes to Generate Answer.
- If no documents match, it routes to No Context Response.
- If retrieval reports an error, it routes to Error Recovery.

All three paths continue to Save Memory and then End.

## 7. Failure Scenario and Recovery

**Failure:** The document retriever encounters an error.

**Cause:** The document retrieval service or component may be unavailable or unable to complete a search.

**Recovery:** The retrieval node records an error in the shared state. Conditional routing detects the error and directs the workflow to the Error Recovery node. The node returns a clear failure message, and the workflow saves the conversation before ending.

In a production system, recovery could also retry retrieval a limited number of times and log the error for debugging.

## 8. Loop Practice

The main program uses a while loop to accept multiple user questions until the user enters `exit`. Each question invokes the graph separately while reusing the conversation-memory list.

The graph itself does not contain a cyclic edge in this version. A retry loop could be added with a retry counter and a maximum-attempt limit.

## 9. Testing

The workflow is tested using:

- A question with matching document information.
- A question without relevant information.
- A question containing `[fail]` to simulate a retrieval failure.

Expected outcomes are a retrieved answer, a no-context response, and a recovery message, respectively.

## 10. Conclusion

This project demonstrates LangGraph nodes, edges, shared state, conditional routing, memory, loop-based interaction, and error recovery. It also illustrates how a graph can route different outcomes through appropriate handling paths instead of allowing a simulated retrieval failure to terminate the workflow.
