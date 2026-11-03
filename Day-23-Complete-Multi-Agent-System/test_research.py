
from agents.research_agent import research_agent
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

result = research_agent(state)

print("\nResearch Agent Output:")
print(result)
