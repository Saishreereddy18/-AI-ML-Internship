# Day 26 – Responsible AI

## 1. Project Overview

This project focuses on understanding Responsible AI principles and implementing a basic Responsible AI Audit Tool.

Responsible AI ensures that Artificial Intelligence systems are fair, transparent, secure, reliable, and accountable.

## 2. Learning Objectives

- Understand AI ethics and responsible AI.
- Learn about bias, hallucination, and privacy risks.
- Understand fairness and transparency.
- Explore human oversight and accountability.
- Implement a basic Responsible AI Proof of Concept.

## 3. Responsible AI Case Study

**Case Study:** Racial Bias in Healthcare AI Algorithm

A healthcare prediction algorithm used healthcare costs to identify patients who needed additional medical support.

Due to differences in healthcare access, the algorithm underestimated the healthcare needs of Black patients.

This demonstrated how biased data and inappropriate prediction targets can create unfair AI decisions.

**Reference:** https://doi.org/10.1126/science.aax2342

## 4. Prevention Recommendations

- Use diverse and representative datasets.
- Perform regular bias audits.
- Protect sensitive personal information.
- Verify AI-generated responses.
- Maintain transparency.
- Include human oversight.
- Monitor AI systems continuously.

## 5. Responsible AI Principles

1. Fairness
2. Privacy
3. Transparency
4. Accountability
5. Reliability
6. Human Oversight

## 6. Company Responsible AI Guidelines

The company should:

- Prevent discrimination in AI applications.
- Protect confidential and personal information.
- Verify AI-generated outputs.
- Document AI models and datasets.
- Include human review for high-impact decisions.
- Monitor deployed AI systems.

## 7. Mini Practical – Responsible AI Audit Tool

**Technology:** Python

**Libraries:** re (regular expressions)

The tool checks AI-generated text for four categories:

1. Bias Detection – Identifies selected biased phrases.
2. Privacy Detection – Identifies possible email addresses and phone numbers.
3. Hallucination Risk – Identifies selected unsupported or exaggerated claims.
4. Human Oversight – Flags selected high-impact decisions for human review.

## 8. Implementation

The Python program uses rule-based checks to identify potential responsible AI risks.

It accepts AI-generated text from the user and generates an audit report.

## 9. Testing Results

| Test                         | Result |
| ---------------------------- | ------ |
| Bias Detection               | Passed |
| Privacy Detection            | Passed |
| Hallucination Risk Detection | Passed |
| Human Oversight              | Passed |

**Total Risk Flags Detected:** 4

**Overall Result:** All four programmed checks worked successfully.

## 10. Execution Instructions

Run the following command:

```bash
python POC/responsible_ai_audit.py
```

Enter AI-generated text when prompted.

The program displays a Responsible AI Audit Report.

## 11. Limitations

- The tool uses predefined rules and keywords.
- It cannot detect every form of bias.
- It cannot verify factual accuracy independently.
- It is a demonstration and not a complete AI safety evaluation system.

## 12. Conclusion

This project demonstrates the importance of Responsible AI in developing trustworthy AI applications.

It combines ethical AI research, prevention recommendations, company guidelines, and a practical Python implementation.
