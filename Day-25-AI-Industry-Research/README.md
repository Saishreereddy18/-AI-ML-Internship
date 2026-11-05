# Day 25 – AI Industry Research

## Overview

This project explores important AI industry developments, including AI trends, cost optimization, and production AI.

It also includes a practical comparison of four AI providers:

- OpenAI
- Anthropic Claude
- Google Gemini
- Groq

## Learning Objectives

- Understand current AI industry trends.
- Learn token usage and API cost optimization.
- Understand production AI requirements.
- Compare AI providers using practical API tests.
- Measure response latency and token consumption.
- Handle API errors and save experiment results.

## Project Structure

```text
Day-25-AI-Industry-Research/
│
├── research/
│   └── AI_Industry_Research_Summary.md
│
├── practical/
│   ├── provider_comparison.py
│   ├── requirements.txt
│   └── .env.example
│
├── results/
│   └── comparison_results.csv
│
├── .env
├── .gitignore
└── README.md
```

## Technologies Used

- Python
- OpenAI API
- Anthropic API
- Google Gemini API
- Groq API
- Pandas
- python-dotenv

## Practical Implementation

The Python program sends three test questions to each configured provider and records:

- Generated answers
- Input and output tokens
- Response latency
- Keyword-based evaluation score
- Provider errors and status

Results are saved in:

`results/comparison_results.csv`

## Observed Results

In the latest experiment:

- OpenAI: API credits unavailable.
- Claude: Insufficient API credits.
- Gemini: Temporary 503 service errors.
- Groq: Three API requests completed.

Groq recorded an average latency of approximately 1.24 seconds and an average keyword score of 50% in the latest run.

These results are limited by provider availability and should not be interpreted as a complete ranking of the four providers.

## How to Run

### 1. Create and activate a virtual environment

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
pip install -r practical/requirements.txt
```

### 3. Configure API keys

Create a `.env` file in the project root and add your provider API keys.

Never upload `.env` or share API keys publicly.

### 4. Run the comparison

```powershell
python practical/provider_comparison.py
```

## Deliverables

1. AI Industry Research Summary.
2. Article reference and key learning points.
3. AI provider comparison program.
4. CSV experiment results.

## Conclusion

This project provided practical experience in AI industry research, LLM API integration, token tracking, latency measurement, error handling, and AI cost optimization.
