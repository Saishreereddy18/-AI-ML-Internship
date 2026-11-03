# Complete Multi-Agent System using LangGraph

## Project Overview

This project demonstrates a complete multi-agent system built using Python and LangGraph. Multiple specialized agents collaborate through a shared state to process user requests, collect information, analyze results, review outputs, and generate final responses.

The project also includes a Career Copilot integration prototype that processes sample AI/ML job results through a separate multi-agent workflow.

## Objectives

- Build a multi-agent architecture using LangGraph.
- Implement communication between specialized agents.
- Manage shared state across agents.
- Implement conditional workflow routing.
- Handle missing data and invalid analysis.
- Demonstrate integration with an AI Career Copilot project.

## Architecture

The system contains five primary agents:

| Agent       | Responsibility                                            |
| ----------- | --------------------------------------------------------- |
| Coordinator | Receives and initializes user requests                    |
| Research    | Collects relevant information from a local knowledge base |
| Analyzer    | Processes research information and creates analysis       |
| Critic      | Reviews analysis and decides whether it is approved       |
| Writer      | Generates the final response after approval               |

### Workflow

User Request → Coordinator → Research → Analyzer → Critic → Writer → Final Answer

The Critic can route rejected, non-empty analysis back to the Analyzer for a limited number of retries. Empty analysis causes safe termination.

## Career Copilot Integration Prototype

A separate workflow accepts sample job-result records through a Career Research Agent.

The adapter extracts:

- Job title
- Company
- Location
- Required skills
- Job description
- Source
- Job URL

The extracted information is passed to the Analyzer, Critic, and Writer agents.

**Note:** This is an integration prototype using supplied sample job data. It does not yet connect directly to live Adzuna or Arbeitnow APIs or the existing AI Career Copilot backend.

## Project Structure

```text
Day-23-Complete-Multi-Agent-System/
│
├── agents/
│   ├── coordinator_agent.py
│   ├── research_agent.py
│   ├── analyzer_agent.py
│   ├── critic_agent.py
│   └── writer_agent.py
│
├── graph/
│   ├── state.py
│   ├── workflow.py
│   └── career_workflow.py
│
├── company_integration/
│   └── career_research_agent.py
│
├── docs/
│   ├── communication_log.md
│   ├── agent_communication_flow.md
│   ├── system_explanation.md
│   ├── error_handling.md
│   ├── company_integration_report.md
│   └── testing_report.md
│
├── diagrams/
│   ├── workflow_diagram.mmd
│   └── sequence_diagram.mmd
│
├── main.py
├── test_state.py
├── test_coordinator.py
├── test_research.py
├── test_analyzer.py
├── test_critic.py
├── test_writer.py
├── test_workflow.py
├── test_career_workflow.py
├── test_career_error.py
├── requirements.txt
└── README.md
```

## Technologies Used

- Python
- LangGraph
- Python-dotenv
- TypedDict
- VS Code
- Git and GitHub

## Installation

Clone the repository or open the project folder.

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Main Workflow

```bash
python main.py
```

## Run Workflow Tests

```bash
python test_workflow.py
```

## Run Career Copilot Integration Test

```bash
python test_career_workflow.py
```

## Run Error Handling Test

```bash
python test_career_error.py
```

## Testing Results

| Test                                 | Result |
| ------------------------------------ | ------ |
| LangGraph workflow compilation       | Passed |
| Main multi-agent workflow            | Passed |
| Career Copilot sample job processing | Passed |
| Missing job results handling         | Passed |

## Error Handling

The system detects missing job results, empty research data, and missing analysis. Errors are stored in the shared state. The workflow prevents the Writer from generating an unapproved response.

## Limitations

- Agent logic currently uses deterministic Python functions and templates, not live LLM calls.
- Research uses a local knowledge base.
- Career Copilot integration currently processes sample job records.
- Live job API integration is a future enhancement.

## Future Enhancements

- Integrate LLM-powered agents.
- Connect live job APIs.
- Add advanced job-skill matching.
- Implement persistent memory.
- Improve agent monitoring and automated testing.

## Conclusion

This project demonstrates multi-agent collaboration, shared state management, conditional routing, workflow validation, error handling, and a Career Copilot integration prototype using LangGraph.

**Project:** Day 23 – Complete Multi-Agent System
