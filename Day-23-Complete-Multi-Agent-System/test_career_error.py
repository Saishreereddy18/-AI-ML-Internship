
from graph.career_workflow import career_copilot_app


# ==========================================
# TEST WITH EMPTY JOB RESULTS
# ==========================================

initial_state = {
    "user_query": "Find AI Engineer jobs",
    "job_results": [],
    "research_data": "",
    "analysis": "",
    "critic_feedback": "",
    "final_answer": "",
    "current_agent": "coordinator",
    "errors": [],
    "retry_count": 0,
    "approved": False
}


print("\n===================================")
print(" CAREER WORKFLOW ERROR TEST")
print("===================================")


# Execute workflow
result = career_copilot_app.invoke(initial_state)


# Display execution results
print("\n===================================")
print(" ERROR TEST SUMMARY")
print("===================================")

print("Current Agent:", result["current_agent"])
print("Approved:", result["approved"])
print("Retry Count:", result["retry_count"])
print("Final Answer:", result["final_answer"])
print("Errors:", result["errors"])


# Verify expected behavior
if (
    not result["approved"]
    and not result["final_answer"]
    and result["errors"]
):
    print("\nERROR HANDLING TEST PASSED!")

else:
    print("\nERROR HANDLING TEST FAILED!")
