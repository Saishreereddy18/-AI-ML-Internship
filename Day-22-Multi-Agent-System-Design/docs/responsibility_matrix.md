# Multi-Agent Responsibility Matrix

## Day 22 – Multi-Agent System Design

### 1. Introduction

A Multi-Agent AI System consists of multiple specialized AI agents working together to complete a complex task. Each agent has a specific responsibility and communicates with other agents by sharing information and intermediate results.

The proposed project is an **AI Research Assistant** that collects information, analyzes findings, checks accuracy, and generates a final research report.

### 2. Agent Responsibility Matrix

| Agent             | Role                                                             | Inputs                          | Outputs                                         | Dependencies             |
| ----------------- | ---------------------------------------------------------------- | ------------------------------- | ----------------------------------------------- | ------------------------ |
| Research Agent    | Collects relevant research information                           | User research query             | Research findings, facts and references         | Coordinator              |
| Analyzer Agent    | Analyzes collected information and identifies important insights | Research findings               | Analysis report and key insights                | Research Agent           |
| Critic Agent      | Reviews findings and identifies errors, gaps and inconsistencies | Research findings and analysis  | Feedback, corrections and validation results    | Research Agent, Analyzer |
| Writer Agent      | Creates a structured research report                             | Validated findings and analysis | Final research report                           | Critic, Analyzer         |
| Coordinator Agent | Manages the complete workflow and assigns tasks                  | User query and agent responses  | Task assignments, shared state and final result | All agents               |

### 3. Agent Responsibilities in Detail

**1. Research Agent**

- Understands the research topic.
- Collects relevant information.
- Identifies useful facts and references.
- Sends findings to the Analyzer and Critic agents.

**2. Analyzer Agent**

- Examines collected research data.
- Identifies important patterns and insights.
- Organizes information into meaningful sections.
- Sends the analysis to the Critic and Writer agents.

**3. Critic Agent**

- Reviews research findings and analysis.
- Checks for missing information and inconsistencies.
- Identifies unsupported claims.
- Sends feedback for corrections.
- Approves the content when it meets quality requirements.

**4. Writer Agent**

- Converts validated information into readable content.
- Organizes the report using headings and sections.
- Prepares the final research document.
- Sends the completed report to the Coordinator.

**5. Coordinator Agent**

- Receives the user's research request.
- Assigns responsibilities to specialized agents.
- Maintains shared state.
- Controls the order of execution.
- Handles communication between agents.
- Collects the final output and delivers it to the user.

### 4. Communication Flow

1. The user submits a research question.
2. The Coordinator receives the request and creates a task.
3. The Research Agent collects relevant information.
4. The Analyzer Agent examines the collected information.
5. The Critic Agent checks the findings and analysis.
6. If corrections are required, feedback is sent to the responsible agent.
7. The Writer Agent prepares the final report using validated information.
8. The Coordinator collects and delivers the completed report.

### 5. Dependencies Between Agents

- Coordinator → Research Agent: Assigns research tasks.
- Research Agent → Analyzer Agent: Shares collected information.
- Research Agent + Analyzer Agent → Critic Agent: Provide content for review.
- Critic Agent → Research/Analyzer Agents: Sends correction feedback when required.
- Critic Agent → Writer Agent: Provides validated content.
- Writer Agent → Coordinator: Submits the final report.

### 6. Shared State

The system maintains a shared state containing:

- Research topic
- User query
- Research findings
- Analysis results
- Critic feedback
- Validation status
- Final research report
- Current workflow status

Each agent reads the information it needs and updates its assigned part of the shared state.

### 7. Conclusion

The Multi-Agent Research Assistant divides a complex research task into smaller responsibilities. By coordinating specialized agents, sharing information and validating results, the system improves workflow organization, content quality and reliability.
