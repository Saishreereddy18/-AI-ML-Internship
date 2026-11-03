
from langgraph.graph import StateGraph, START, END

from graph.state import AgentState

from agents.coordinator_agent import coordinator_agent
from agents.analyzer_agent import analyzer_agent
from agents.critic_agent import critic_agent
from agents.writer_agent import writer_agent

from company_integration.career_research_agent import (
    career_research_agent
)


# ==========================================
# 1. CREATE CAREER COPILOT WORKFLOW
# ==========================================

career_workflow = StateGraph(AgentState)


# ==========================================
# 2. REGISTER AGENTS
# ==========================================

career_workflow.add_node(
    "coordinator",
    coordinator_agent
)

career_workflow.add_node(
    "career_research",
    career_research_agent
)

career_workflow.add_node(
    "analyzer",
    analyzer_agent
)

career_workflow.add_node(
    "critic",
    critic_agent
)

career_workflow.add_node(
    "writer",
    writer_agent
)


# ==========================================
# 3. DEFINE EXECUTION FLOW
# ==========================================

career_workflow.add_edge(
    START,
    "coordinator"
)

career_workflow.add_edge(
    "coordinator",
    "career_research"
)

career_workflow.add_edge(
    "career_research",
    "analyzer"
)

career_workflow.add_edge(
    "analyzer",
    "critic"
)


# ==========================================
# 4. CRITIC CONDITIONAL ROUTING
# ==========================================

def career_critic_decision(state):

    if not state.get("analysis", "").strip():

        print("\n[Career Workflow] Empty analysis.")
        return "end"

    if state.get("approved", False):

        print("\n[Career Workflow] Analysis approved.")
        return "writer"

    if state.get("retry_count", 0) < 2:

        print("\n[Career Workflow] Retrying Analyzer.")
        return "analyzer"

    print("\n[Career Workflow] Retry limit reached.")
    return "end"


career_workflow.add_conditional_edges(
    "critic",
    career_critic_decision,
    {
        "writer": "writer",
        "analyzer": "analyzer",
        "end": END
    }
)


# ==========================================
# 5. WRITER COMPLETES THE WORKFLOW
# ==========================================

career_workflow.add_edge(
    "writer",
    END
)


# ==========================================
# 6. COMPILE WORKFLOW
# ==========================================

career_copilot_app = career_workflow.compile()


print("Career Copilot Workflow compiled successfully!")
