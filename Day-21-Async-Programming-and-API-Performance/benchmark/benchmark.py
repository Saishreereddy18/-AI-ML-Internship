
import asyncio
import httpx
import time
import csv
from pathlib import Path
from statistics import mean

# Project configuration
BASE_DIR = Path(__file__).resolve().parent.parent

PDF_PATH = Path(r"C:\Users\saish\Downloads\Saishree_resume.pdf")


OLD_API = "http://127.0.0.1:8001"
NEW_API = "http://127.0.0.1:8000"

REQUESTS_PER_ROUND = 20
ROUNDS = 3

QUESTION = "What are my technical skills and programming languages?"

RESULTS_FILE = BASE_DIR / "benchmark" / "results.csv"


async def upload_pdf(client, url, endpoint):
    with open(PDF_PATH, "rb") as pdf:
        response = await client.post(
            f"{url}{endpoint}",
            files={"file": ("Saishree_resume.pdf", pdf, "application/pdf")}
        )

    response.raise_for_status()
    return response.json()["document_id"]


async def benchmark_api(client, url, endpoint, document_id):
    async def send_request():
        start = time.perf_counter()

        response = await client.post(
            f"{url}{endpoint}/{document_id}",
            json={"question": QUESTION}
        )

        elapsed = time.perf_counter() - start
        response.raise_for_status()
        return elapsed

    start_total = time.perf_counter()

    timings = await asyncio.gather(
        *[send_request() for _ in range(REQUESTS_PER_ROUND)]
    )

    total_time = time.perf_counter() - start_total

    return {
        "average_latency_ms": round(mean(timings) * 1000, 3),
        "total_time_seconds": round(total_time, 3),
        "throughput_requests_per_second": round(
            REQUESTS_PER_ROUND / total_time, 3
        )
    }


async def main():
    if not PDF_PATH.exists():
        print(f"ERROR: PDF not found: {PDF_PATH}")
        return

    timeout = httpx.Timeout(60.0)

    async with httpx.AsyncClient(timeout=timeout) as client:

        print("Uploading PDF to Day 17 API...")
        old_id = await upload_pdf(client, OLD_API, "/upload")

        print("Uploading PDF to Day 21 API...")
        new_id = await upload_pdf(client, NEW_API, "/api/v1/upload")

        print("\nPDF upload successful!")
        print("Starting performance benchmark...\n")

        results = []

        for round_number in range(1, ROUNDS + 1):
            print(f"Benchmark Round {round_number}/{ROUNDS}")

            # Alternate execution order to reduce ordering bias.
            if round_number % 2 == 1:
                old_result = await benchmark_api(
                    client, OLD_API, "/ask", old_id
                )
                new_result = await benchmark_api(
                    client, NEW_API, "/api/v1/ask", new_id
                )
            else:
                new_result = await benchmark_api(
                    client, NEW_API, "/api/v1/ask", new_id
                )
                old_result = await benchmark_api(
                    client, OLD_API, "/ask", old_id
                )

            results.append(("Day 17 - Sync", round_number, old_result))
            results.append(("Day 21 - Async", round_number, new_result))

            print("Day 17:", old_result)
            print("Day 21:", new_result)
            print()

        RESULTS_FILE.parent.mkdir(parents=True, exist_ok=True)

        with open(RESULTS_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow([
                "API",
                "Round",
                "Average Latency (ms)",
                "Total Time (seconds)",
                "Throughput (requests/second)"
            ])

            for api_name, round_number, result in results:
                writer.writerow([
                    api_name,
                    round_number,
                    result["average_latency_ms"],
                    result["total_time_seconds"],
                    result["throughput_requests_per_second"]
                ])

        print("Benchmark completed successfully!")
        print(f"Results saved to: {RESULTS_FILE}")


if __name__ == "__main__":
    asyncio.run(main())
