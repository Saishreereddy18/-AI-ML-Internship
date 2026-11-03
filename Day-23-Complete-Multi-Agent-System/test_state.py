from graph.state import AgentState

state: AgentState = {
    "user_query": "Explain Multi-Agent Systems",
    "research_data": "",
    "analysis": "",
    "critic_feedback": "",
    "final_answer": "",
    "current_agent": "coordinator",
    "errors": [],
    "retry_count": 0,
    "approved": False
}

print("STATE MANAGEMENT TEST")
print("---------------------")

print("User Query:", state["user_query"])
print("Current Agent:", state["current_agent"])
print("Retry Count:", state["retry_count"])
print("Approved:", state["approved"])

print("\nState initialized successfully!")