
def research_agent(state):

    print("\n[Research Agent]")
    print("Researching the user query...")

    query = state["user_query"]

    # Basic research knowledge for our initial implementation
    knowledge_base = {
        "multi-agent systems": (
            "Multi-Agent Systems consist of multiple "
            "independent AI agents working together "
            "to achieve a common goal."
        ),
        "artificial intelligence": (
            "Artificial Intelligence enables machines "
            "to perform tasks that normally require "
            "human intelligence."
        ),
        "machine learning": (
            "Machine Learning is a branch of AI that "
            "allows systems to learn patterns from data."
        )
    }

    # Search for relevant information
    research_result = None

    for topic, information in knowledge_base.items():
        if topic in query.lower():
            research_result = information
            break

    if research_result is None:
        research_result = (
            f"Initial research completed for: {query}. "
            "Further external research may be required."
        )

    print("Research completed.")
    print("Findings:", research_result)

    return {
        "research_data": research_result,
        "current_agent": "research"
    }
