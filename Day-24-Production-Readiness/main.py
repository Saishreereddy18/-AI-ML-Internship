
from logger_config import logger
from graph.workflow import multi_agent_app

logger.info("AI Career Copilot started")


def run_multi_agent_system(user_query):

    logger.info("Running multi-agent system with query: %s", user_query)

    print("\n===================================")
    print(" COMPLETE MULTI-AGENT SYSTEM")
    print("===================================")

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

        result = multi_agent_app.invoke(initial_state)

        logger.info("Workflow executed successfully")

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

        logger.info(
            "Execution completed | Approved: %s | Retries: %s",
            result["approved"],
            result["retry_count"]
        )

        return result

    except Exception:

        logger.exception("AI Career Copilot workflow failed")
        print("\nWorkflow execution failed. Check logs/app.log")

        return None


if __name__ == "__main__":

    query = input("\nEnter your question: ")

    run_multi_agent_system(query)
