\# Architecture Notes

\## Day 22 – Multi-Agent System Design

\### Project: AI Research Assistant



\### 1. Architecture Overview



The AI Research Assistant follows a Coordinator-Based Multi-Agent Architecture.



The system consists of five specialized AI agents that collaborate to collect, analyze, validate and generate research information.



Each agent performs an independent responsibility while communicating through structured messages and shared state.



\### 2. Main Architecture Components



| Component | Responsibility |

|---|---|

| User Interface | Accepts research queries from users |

| Coordinator Agent | Controls workflow and assigns tasks |

| Research Agent | Collects relevant information |

| Analyzer Agent | Processes and analyzes findings |

| Critic Agent | Validates information and provides feedback |

| Writer Agent | Generates the final research report |

| Shared State | Stores intermediate results and workflow information |

| Output Generator | Delivers the final report |



\### 3. Agent Interaction Architecture



The system follows this execution sequence:



1\. User submits a research query.

2\. Coordinator initializes the workflow.

3\. Research Agent collects information.

4\. Analyzer processes the collected information.

5\. Critic validates the results.

6\. If corrections are required, the workflow returns to the relevant agent.

7\. Writer prepares the final report.

8\. Coordinator delivers the output.



\### 4. Communication Architecture



Agents communicate using structured messages.



Each message contains:

\- Sender agent.

\- Receiver agent.

\- Task identifier.

\- Message type.

\- Input or output content.

\- Execution status.



The Coordinator manages task routing, while the shared state maintains information between workflow stages.



\### 5. Shared State Architecture



Shared state acts as a centralized information structure.



Example:



```python

state = {

&#x20;   "research\_query": "",

&#x20;   "research\_findings": \[],

&#x20;   "analysis\_results": {},

&#x20;   "critic\_feedback": \[],

&#x20;   "validation\_status": "pending",

&#x20;   "final\_report": "",

&#x20;   "workflow\_status": "initialized",

&#x20;   "retry\_count": 0

}

```



Each agent accesses the information required for its task and updates its respective output fields.



\### 6. Workflow Control



The Coordinator controls the execution using conditional decisions.



| Condition | Next Action |

|---|---|

| Research completed | Start analysis |

| Analysis completed | Start validation |

| Validation approved | Start writing |

| Validation rejected | Request corrections |

| Maximum retries reached | Stop and report unresolved issues |

| Report completed | Deliver final output |



A maximum retry limit prevents infinite execution loops.



\### 7. Architecture Design Principles



\- \*\*Modularity:\*\* Each agent has a separate responsibility.

\- \*\*Reusability:\*\* Agents can be reused in other workflows.

\- \*\*Scalability:\*\* New agents can be added when required.

\- \*\*Communication:\*\* Agents exchange structured information.

\- \*\*Reliability:\*\* Critic validation improves output quality.

\- \*\*Maintainability:\*\* Individual agents can be modified independently.



\### 8. Connection with LangGraph



The proposed architecture can be implemented using LangGraph.



| LangGraph Concept | Application |

|---|---|

| State | Shared workflow information |

| Nodes | Individual AI agents |

| Edges | Agent communication paths |

| Conditional Edges | Validation-based decisions |

| Checkpointing | Workflow state persistence |

| Graph | Complete multi-agent workflow |



\### 9. Conclusion



The proposed architecture provides a structured foundation for implementing a collaborative AI Research Assistant. The combination of specialized agents, shared state, communication and conditional workflow control makes the system modular, scalable and easier to maintain.

