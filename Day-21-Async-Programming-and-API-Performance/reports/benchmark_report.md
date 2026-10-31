# Day 21 – Benchmark Report

## 1. Introduction

This benchmark evaluates the performance of the Day 21 asynchronous RAG API against the original Day 17 synchronous RAG API.

The objective is to understand how asynchronous programming affects API response time and request handling under concurrent workloads.

## 2. Benchmark Configuration

| Parameter              | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| Original API           | Day 17 – Synchronous RAG API                            |
| Updated API            | Day 21 – Asynchronous RAG API                           |
| Testing library        | HTTPX                                                   |
| Concurrent requests    | 20 per round                                            |
| Benchmark rounds       | 3                                                       |
| Total requests per API | 60                                                      |
| Input document         | Saishree_resume.pdf                                     |
| Question               | What are my technical skills and programming languages? |

## 3. Benchmark Results

| Round | Day 17 Latency (ms) | Day 21 Latency (ms) |
| ----- | ------------------: | ------------------: |
| 1     |             143.973 |             112.466 |
| 2     |              89.266 |              95.645 |
| 3     |              80.943 |             109.066 |

### Overall Results

| Metric             |          Day 17 |          Day 21 |
| ------------------ | --------------: | --------------: |
| Average latency    |      104.727 ms |      105.726 ms |
| Average total time |       0.150 sec |       0.156 sec |
| Average throughput | 135.720 req/sec | 128.449 req/sec |

## 4. Analysis

1. The asynchronous API achieved lower latency in the first round.
2. The synchronous API achieved lower latency in the second and third rounds.
3. The original API showed slightly lower overall average latency.
4. The original API also achieved higher average throughput.
5. The asynchronous implementation provides a structure for handling asynchronous I/O operations and background tasks.

## 5. Key Learning Outcomes

- Understanding async and await in Python.
- Implementing asynchronous FastAPI endpoints.
- Using background tasks for non-blocking operations.
- Creating custom middleware to measure request processing time.
- Using dependency injection to manage shared resources.
- Applying request validation with Pydantic.
- Comparing API performance using concurrent HTTP requests.

## 6. Final Conclusion

The Day 21 asynchronous RAG API was implemented and tested successfully.

The benchmark showed that asynchronous programming did not automatically improve performance for this particular lightweight workload. The results demonstrate the importance of measuring actual performance rather than assuming that asynchronous code is always faster.

Further experiments with heavier workloads and I/O-intensive operations can help evaluate the scalability benefits of asynchronous programming.

## 7. Generated Files

- benchmark.py – Performance testing script.
- results.csv – Raw benchmark measurements.
- performance_comparison.md – Comparative analysis.
- benchmark_report.md – Complete benchmark report.
