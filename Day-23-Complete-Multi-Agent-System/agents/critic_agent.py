
def critic_agent(state):

    print("\n[Critic Agent]")
    print("Reviewing the analysis...")

    analysis = state.get("analysis", "")
    errors = state.get("errors", [])
    retry_count = state.get("retry_count", 0)

    # Check whether analysis is available
    if not analysis.strip():

        feedback = "Analysis is missing."
        approved = False

        errors = errors + [
            "Critic rejected empty analysis."
        ]

    else:

        # Required sections for approval
        required_sections = [
            "Key Insight",
            "Benefit",
            "Application"
        ]

        missing_sections = [
            section
            for section in required_sections
            if section not in analysis
        ]

        if missing_sections:

            feedback = (
                "Missing information: "
                + ", ".join(missing_sections)
            )

            approved = False

        else:

            feedback = (
                "Analysis is complete, relevant "
                "and contains all required sections."
            )

            approved = True

    # Increment retry count only when rejected
    if not approved:
        retry_count += 1

    print("Critic Feedback:", feedback)
    print("Approved:", approved)
    print("Retry Count:", retry_count)

    return {
        "critic_feedback": feedback,
        "approved": approved,
        "current_agent": "critic",
        "retry_count": retry_count,
        "errors": errors
    }
