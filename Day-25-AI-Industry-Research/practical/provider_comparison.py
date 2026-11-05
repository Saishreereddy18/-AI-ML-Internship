
import os
import time
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI
from anthropic import Anthropic
from google import genai
from groq import Groq

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_DIR / ".env")

RESULTS_DIR = PROJECT_DIR / "results"
RESULTS_DIR.mkdir(exist_ok=True)

# Provider configuration
PROVIDERS = {
    "OpenAI": {
        "key": os.getenv("OPENAI_API_KEY"),
        "model": os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
    },
    "Claude": {
        "key": os.getenv("ANTHROPIC_API_KEY"),
        "model": os.getenv("CLAUDE_MODEL", "claude-haiku-4-5-20251001"),
    },
    "Gemini": {
        "key": os.getenv("GEMINI_API_KEY"),
        "model": os.getenv("GEMINI_MODEL", "gemini-3.8-flash"),
    },
    "Groq": {
        "key": os.getenv("GROQ_API_KEY"),
        "model": os.getenv("GROQ_MODEL", "openai/gpt-oss-20b"),
    },
}

TEST_CASES = [
    {
        "question": "Explain the difference between a Python list and tuple in two sentences.",
        "keywords": ["list", "tuple", "mutable", "immutable"],
    },
    {
        "question": "What does HTTP status code 404 mean? Answer briefly.",
        "keywords": ["404", "not found"],
    },
    {
        "question": "Explain Retrieval-Augmented Generation (RAG) in simple words.",
        "keywords": ["retriev", "document", "context", "generat"],
    },
]


def ask_provider(provider, config, question):
    key = config["key"]
    model = config["model"]

    if not key or key.startswith("your_"):
        raise ValueError("API key is missing. Provider skipped.")

    start = time.time()

    if provider == "OpenAI":
        client = OpenAI(api_key=key, timeout=20.0)
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": question}],
            max_tokens=200,
        )
        answer = response.choices[0].message.content or ""
        usage = response.usage
        input_tokens = usage.prompt_tokens if usage else 0
        output_tokens = usage.completion_tokens if usage else 0

    elif provider == "Claude":
        client = Anthropic(api_key=key, timeout=20.0)
        response = client.messages.create(
            model=model,
            max_tokens=200,
            messages=[{"role": "user", "content": question}],
        )
        answer = "".join(
            block.text for block in response.content
            if hasattr(block, "text")
        )
        input_tokens = response.usage.input_tokens
        output_tokens = response.usage.output_tokens

    elif provider == "Gemini":
        client = genai.Client(api_key=key)
        response = client.models.generate_content(
            model=model,
            contents=question,
        )
        answer = response.text or ""
        usage = response.usage_metadata
        input_tokens = usage.prompt_token_count if usage else 0
        output_tokens = usage.candidates_token_count if usage else 0

    elif provider == "Groq":
        client = Groq(api_key=key, timeout=20.0)
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": question}],
            max_tokens=200,
        )
        answer = response.choices[0].message.content or ""
        usage = response.usage
        input_tokens = usage.prompt_tokens if usage else 0
        output_tokens = usage.completion_tokens if usage else 0

    else:
        raise ValueError("Unknown provider")

    latency = round(time.time() - start, 2)

    return answer, input_tokens, output_tokens, latency


def evaluate_answer(answer, keywords):
    if not answer:
        return 0

    answer_lower = answer.lower()
    matches = sum(
        1 for word in keywords if word.lower() in answer_lower
    )
    return round(matches / len(keywords) * 100, 2)


def main():
    print("\n" + "=" * 55)
    print(" DAY 25 - AI PROVIDER COMPARISON")
    print("=" * 55)

    results = []

    for provider, config in PROVIDERS.items():
        print(f"\nTesting Provider: {provider}")
        print("-" * 45)

        for index, test in enumerate(TEST_CASES, start=1):
            print(f"\nQuestion {index}: {test['question']}")

            record = {
                "Provider": provider,
                "Model": config["model"],
                "Question": test["question"],
                "Answer": "",
                "Input Tokens": 0,
                "Output Tokens": 0,
                "Latency (seconds)": None,
                "Keyword Score (%)": None,
                "Status": "Failed",
                "Error": "",
            }

            try:
                answer, input_tokens, output_tokens, latency = (
                    ask_provider(provider, config, test["question"])
                )

                score = evaluate_answer(answer, test["keywords"])

                record.update({
                    "Answer": answer,
                    "Input Tokens": input_tokens,
                    "Output Tokens": output_tokens,
                    "Latency (seconds)": latency,
                    "Keyword Score (%)": score,
                    "Status": "Success",
                })

                print("Answer:", answer)
                print("Latency:", latency, "seconds")
                print("Input tokens:", input_tokens)
                print("Output tokens:", output_tokens)
                print("Keyword score:", score, "%")

            except Exception as error:
                record["Error"] = str(error)[:500]
                print("Provider unavailable:", record["Error"])
                print("Continuing to next test...")

                # Short pause after a temporary provider error
                time.sleep(1)

            results.append(record)

    # Save all results, including failures
    output_file = RESULTS_DIR / "comparison_results.csv"
    df = pd.DataFrame(results)
    df.to_csv(output_file, index=False)

    print("\n" + "=" * 55)
    print(" COMPARISON SUMMARY")
    print("=" * 55)

    successful = df[df["Status"] == "Success"]

    if not successful.empty:
        summary = successful.groupby("Provider").agg(
            Average_Latency=("Latency (seconds)", "mean"),
            Average_Keyword_Score=("Keyword Score (%)", "mean"),
            Successful_Tests=("Status", "count"),
        )
        print(summary.round(2))
    else:
        print("No provider completed a successful test.")

    print("\nResults saved to:", output_file)
    print("Day 25 comparison completed.")


if __name__ == "__main__":
    main()
