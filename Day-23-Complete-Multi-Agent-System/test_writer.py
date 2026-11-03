from agents.writer_agent import writer_agent
from graph.state import AgentState

state: AgentState = {
    "user_query": "Explain Multi-Agent Systems",
    "research_data": "Multiple AI agents work together.",
    "analysis": (
        "Analysis Summary:\n"
        "1. Key Insight: Agents divide tasks.\n"
        "2. Benefit: Better collaboration.\n"
        "3. Application: Research and automation."
    ),
    "critic_feedback": (
        "Analysis is complete, relevant "
        "and contains all required sections."
    ),
    "final_answer": "",
    "current_agent": "critic",
    "errors": [],
    "retry_count": 0,
    "approved": True
}

result = writer_agent(state)

print("\nWriter Agent Output:")
print(result["final_answer"])