
def writer_agent(state):

    print("\n[Writer Agent]")
    print("Generating final response...")

    analysis = state["analysis"]
    feedback = state["critic_feedback"]
    approved = state["approved"]

    # Check critic approval
    if not approved:

        print("Writer cannot proceed.")
        print("Reason: Critic has not approved the analysis.")

        return {
            "final_answer": "",
            "current_agent": "writer",
            "errors": state.get("errors", []) + [
                "Writer blocked: Analysis not approved."
            ]
        }

    # Generate the final response
    final_response = (
        "FINAL RESPONSE\n"
        "===============\n\n"
        f"User Question: {state['user_query']}\n\n"
        f"{analysis}\n\n"
        f"Review Status: {feedback}\n\n"
        "Conclusion: Multi-Agent Systems allow "
        "multiple specialized AI agents to collaborate "
        "and solve complex tasks efficiently."
    )

    print("Final response generated successfully.")

    return {
        "final_answer": final_response,
        "current_agent": "writer"
    }
