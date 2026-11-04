
def analyzer_agent(state):

    print("\n[Analyzer Agent]")
    print("Analyzing research findings...")

    research_data = state.get("research_data", "")

    if not research_data.strip():

        error_message = "Analyzer received empty research data."

        print("Error:", error_message)

        return {
            "analysis": "",
            "current_agent": "analyzer",
            "errors": state.get("errors", []) + [
                error_message
            ]
        }

    analysis_result = (
        "Analysis Summary:\n"
        f"Research Information: {research_data}\n"
        "Key Insight: Multiple agents divide complex tasks.\n"
        "Benefit: Better collaboration and efficiency.\n"
        "Application: Research, analysis and automation."
    )

    print("Analysis completed.")
    print(analysis_result)

    return {
        "analysis": analysis_result,
        "current_agent": "analyzer"
    }
