# Day 21 – Performance Comparison Report

## 1. Objective

To compare the performance of the original synchronous RAG API (Day 17) with the upgraded asynchronous RAG API (Day 21).

## 2. Testing Environment

- Framework: FastAPI
- Language: Python
- Testing tool: HTTPX
- Concurrent requests per round: 20
- Number of benchmark rounds: 3
- Test document: Saishree_resume.pdf
- Day 17 API: http://127.0.0.1:8001
- Day 21 API: http://127.0.0.1:8000

## 3. Benchmark Results

| Metric                  |   Day 17 – Sync |  Day 21 – Async |
| ----------------------- | --------------: | --------------: |
| Round 1 Average Latency |      143.973 ms |      112.466 ms |
| Round 2 Average Latency |       89.266 ms |       95.645 ms |
| Round 3 Average Latency |       80.943 ms |      109.066 ms |
| Overall Average Latency |      104.727 ms |      105.726 ms |
| Average Total Time      |       0.150 sec |       0.156 sec |
| Average Throughput      | 135.720 req/sec | 128.449 req/sec |

## 4. Performance Observations

- Day 21 performed better in the first benchmark round.
- Day 17 performed better in the second and third rounds.
- Overall average latency was slightly lower for Day 17.
- Day 17 also achieved higher average throughput.
- Results varied between rounds, showing that performance can be affected by system load and request scheduling.

## 5. Conclusion

The Day 21 API successfully implements asynchronous endpoints, background tasks, middleware, dependency injection, and validation.

The benchmark did not show an overall performance improvement over Day 17 for this lightweight PDF question-answering workload.

Asynchronous programming improves the ability to handle I/O-bound operations efficiently, but it does not automatically guarantee lower response times. Further testing with heavier workloads and more realistic I/O operations would help evaluate its benefits.

## 6. Deliverables

- Benchmark script: benchmark/benchmark.py
- Benchmark results: benchmark/results.csv
- Performance comparison: reports/performance_comparison.md
- Updated API documentation: Swagger UI at /docs
