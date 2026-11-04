
def coordinator_agent(state):

    print("\n[Coordinator Agent]")
    print("Received user request.")

    user_query = state["user_query"]

    print("User Query:", user_query)

    return {
        "current_agent": "coordinator",
        "errors": state.get("errors", [])
    }
