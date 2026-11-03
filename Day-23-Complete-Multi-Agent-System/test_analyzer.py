
from agents.analyzer_agent import analyzer_agent
from graph.state import AgentState

state: AgentState = {
    "user_query": "Explain Multi-Agent Systems",
    "research_data": (
        "Multi-Agent Systems consist of multiple "
        "independent AI agents working together "
        "to achieve a common goal."
    ),
    "analysis": "",
    "critic_feedback": "",
    "final_answer": "",
    "current_agent": "research",
    "errors": [],
    "retry_count": 0,
    "approved": False
}

result = analyzer_agent(state)

print("\nAnalyzer Agent Output:")
print(result)
