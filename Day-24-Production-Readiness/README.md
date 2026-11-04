# AI Career Copilot – Production Readiness

## Project Overview

AI Career Copilot is a Python-based multi-agent system developed using LangGraph. It uses specialized AI agents to coordinate tasks, research information, analyze results, review outputs and generate final responses.

## Technologies Used

- Python
- LangGraph
- Pytest
- Python Logging
- Python-dotenv
- Docker

## Project Structure

```text
Day-24-Production-Readiness/
│
├── agents/
├── company_integration/
├── graph/
├── tests/
│   ├── test_unit.py
│   └── test_api.py
│
├── logs/
├── main.py
├── logger_config.py
├── .env
├── .env.example
├── .gitignore
├── .dockerignore
├── Dockerfile
├── requirements.txt
├── DEPLOYMENT_CHECKLIST.md
├── PRODUCTION_READINESS_REPORT.md
└── README.md
```

## Features

- Multi-agent workflow execution.
- Automated research and analysis.
- Critic-based response validation.
- Pytest unit testing.
- Application logging.
- Environment variable configuration.
- Docker deployment configuration.

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate to the project:

```bash
cd Day-24-Production-Readiness
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure environment variables:

```bash
copy .env.example .env
```

## Run the Application

```bash
python main.py
```

Enter a query when prompted.

## Run Tests

```bash
python -m pytest tests/ -v
```

Note: API tests are not implemented because the current project does not expose HTTP endpoints.

## Logging

Application logs are generated in:

```text
logs/app.log
```

Logs capture application startup, execution status and errors.

## Docker

Docker configuration is provided through the Dockerfile and .dockerignore.

Docker image build and container execution are pending verification because Docker is not installed in the development environment.

## Documentation

- DEPLOYMENT_CHECKLIST.md – Deployment requirements.
- PRODUCTION_READINESS_REPORT.md – Production readiness assessment.

## Production Readiness

The project includes testing preparation, logging, environment configuration and Docker configuration.

Full production deployment requires additional testing, Docker verification, security checks and monitoring.

## Author

Billa Sai Sree
