
from graph.workflow import multi_agent_app


def run_multi_agent_system(user_query):

    print("\n===================================")
    print(" COMPLETE MULTI-AGENT SYSTEM")
    print("===================================")

    # Initialize shared state
    initial_state = {
        "user_query": user_query,
        "research_data": "",
        "analysis": "",
        "critic_feedback": "",
        "final_answer": "",
        "current_agent": "coordinator",
        "errors": [],
        "retry_count": 0,
        "approved": False
    }

    try:

        # Execute all agents through LangGraph
        result = multi_agent_app.invoke(initial_state)

        print("\n===================================")
        print(" FINAL SYSTEM RESPONSE")
        print("===================================")

        if result.get("final_answer"):
            print(result["final_answer"])

        else:
            print("Workflow could not generate an approved answer.")
            print("Critic Feedback:", result.get("critic_feedback", ""))

        print("\n===================================")
        print(" EXECUTION SUMMARY")
        print("===================================")

        print("Current Agent:", result["current_agent"])
        print("Retry Count:", result["retry_count"])
        print("Approved:", result["approved"])
        print("Errors:", result["errors"])

        return result

    except Exception as error:

        print("\nWorkflow Error:", str(error))

        return None


if __name__ == "__main__":

    query = input("\nEnter your question: ")

    run_multi_agent_system(query)
