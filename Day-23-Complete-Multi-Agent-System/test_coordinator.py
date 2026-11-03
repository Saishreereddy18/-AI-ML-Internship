from agents.coordinator_agent import coordinator_agent
from graph.state import AgentState

state: AgentState = {
    "user_query": "Explain Multi-Agent Systems",
    "research_data": "",
    "analysis": "",
    "critic_feedback": "",
    "final_answer": "",
    "current_agent": "",
    "errors": [],
    "retry_count": 0,
    "approved": False
}

result = coordinator_agent(state)

print("\nCoordinator Output:")
print(result)