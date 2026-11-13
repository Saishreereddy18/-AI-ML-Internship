# Day 27 – Task Priority Table

| Task                 | Business Value | Complexity | Priority | Dependency          |
| -------------------- | -------------- | ---------- | -------- | ------------------- |
| Requirement analysis | High           | Medium     | High     | None                |
| Resume upload        | High           | Medium     | High     | Requirements        |
| Text extraction      | High           | Medium     | High     | Resume upload       |
| Skill extraction     | High           | High       | High     | Text extraction     |
| Job API integration  | High           | High       | High     | Requirements        |
| Job matching         | High           | High       | High     | Skills + Job API    |
| Skill gap analysis   | Medium         | Medium     | Medium   | Job matching        |
| Resume generation    | Medium         | High       | Medium   | Resume analysis     |
| Frontend integration | High           | High       | Medium   | Backend APIs        |
| Testing              | High           | Medium     | High     | Feature development |
| Deployment           | Medium         | Medium     | Low      | Testing             |

## Priority Explanation

- High: Essential tasks that must be completed first.
- Medium: Important tasks that follow core development.
- Low: Tasks that can be completed towards the end.
