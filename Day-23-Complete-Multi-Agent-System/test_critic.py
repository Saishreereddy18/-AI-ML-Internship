
from agents.critic_agent import critic_agent
from graph.state import AgentState

state: AgentState = {
    "user_query": "Explain Multi-Agent Systems",
    "research_data": (
        "Multiple AI agents work together."
    ),
    "analysis": (
        "Analysis Summary:\n"
        "1. Key Insight: Agents divide tasks.\n"
        "2. Benefit: Better collaboration.\n"
        "3. Application: Research and automation."
    ),
    "critic_feedback": "",
    "final_answer": "",
    "current_agent": "analyzer",
    "errors": [],
    "retry_count": 0,
    "approved": False
}

result = critic_agent(state)

print("\nCritic Agent Output:")
print(result)
