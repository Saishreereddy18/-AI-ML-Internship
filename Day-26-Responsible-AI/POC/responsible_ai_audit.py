
import re

# Responsible AI Audit Tool

def check_bias(text):
    biased_terms = [
        "all women are",
        "all men are",
        "people from this race are",
        "people with disabilities cannot",
        "only men can",
        "only women can"
    ]

    return [term for term in biased_terms if term in text.lower()]


def check_privacy(text):
    issues = []

    email_pattern = r'\b[\w.-]+@[\w.-]+\.\w+\b'
    phone_pattern = r'\b(?:\+91[- ]?)?[6-9]\d{9}\b'

    if re.search(email_pattern, text):
        issues.append("Possible email address detected")

    if re.search(phone_pattern, text):
        issues.append("Possible phone number detected")

    return issues


def check_hallucination_risk(text):
    risky_phrases = [
        "100% guaranteed",
        "definitely cures",
        "completely risk-free",
        "guaranteed results",
        "always correct"
    ]

    return [
        phrase for phrase in risky_phrases
        if phrase in text.lower()
    ]


def check_human_oversight(text):
    high_impact_keywords = [
        "medical diagnosis",
        "loan approval",
        "hiring decision",
        "legal decision",
        "patient treatment"
    ]

    return any(
        keyword in text.lower()
        for keyword in high_impact_keywords
    )


def audit_ai_output(text):

    print("\n" + "=" * 45)
    print("       RESPONSIBLE AI AUDIT REPORT")
    print("=" * 45)

    bias = check_bias(text)
    privacy = check_privacy(text)
    hallucination = check_hallucination_risk(text)
    human_review = check_human_oversight(text)

    print("\n1. BIAS CHECK")
    if bias:
        print("WARNING: Potential biased language detected.")
        print("Matched terms:", bias)
    else:
        print("No listed bias-related phrases detected.")

    print("\n2. PRIVACY CHECK")
    if privacy:
        print("WARNING: Possible personal information detected.")
        for issue in privacy:
            print("-", issue)
    else:
        print("No listed personal information patterns detected.")

    print("\n3. HALLUCINATION RISK CHECK")
    if hallucination:
        print("WARNING: Potentially unsupported claims detected.")
        print("Matched phrases:", hallucination)
    else:
        print("No listed risky phrases detected.")

    print("\n4. HUMAN OVERSIGHT CHECK")
    if human_review:
        print("REVIEW REQUIRED: High-impact decision detected.")
        print("A qualified human should review the output.")
    else:
        print("No listed high-impact decision detected.")

    total_issues = (
        len(bias)
        + len(privacy)
        + len(hallucination)
        + int(human_review)
    )

    print("\n" + "-" * 45)
    print("TOTAL FLAGS:", total_issues)

    if total_issues == 0:
        print("Result: No listed risks detected.")
    else:
        print("Result: Further review is recommended.")

    print("=" * 45)


# Main Program

if __name__ == "__main__":

    print("RESPONSIBLE AI AUDIT TOOL")
    print("-------------------------")

    ai_output = input(
        "\nEnter AI-generated text to audit:\n"
    )

    if ai_output.strip():
        audit_ai_output(ai_output)
    else:
        print("Please enter some text.")
