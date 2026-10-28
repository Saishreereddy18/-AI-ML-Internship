# Day 19 – Error Handling Notes

## Purpose

To identify possible workflow failures and define recovery strategies using LangGraph conditional routing.

| Failure Scenario          | Detection                        | Recovery Action                               |
| ------------------------- | -------------------------------- | --------------------------------------------- |
| Retrieval error           | Error field is not empty         | Route to Error Recovery                       |
| No matching documents     | Retrieved document list is empty | Return a no-context response                  |
| Empty user question       | Input validation                 | Ask the user to enter a question              |
| Unexpected Python error   | Exception handling               | Display a retry message                       |
| Temporary service failure | Service error or timeout         | Retry a limited number of times in production |

## Conditional Routing Logic

1. Check whether the retrieval node reported an error.
2. If an error exists, route to Error Recovery.
3. Otherwise, check whether relevant documents were found.
4. If documents exist, route to Generate Answer.
5. If no documents exist, route to No Context Response.
6. Save the resulting conversation and end the graph.

## Important Notes

- Error messages should be clear and useful.
- Retry mechanisms should have a maximum-attempt limit.
- Errors should be logged for debugging in production.
- Conversation memory in the current implementation is temporary and is not persistent across program restarts.
- The current graph handles retrieval failures; a production implementation should also handle LLM errors and external service timeouts.

## Result

Conditional routing allows the workflow to handle different outcomes and recover from the simulated retrieval failure without crashing the normal graph execution.
