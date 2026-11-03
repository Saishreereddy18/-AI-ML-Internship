
from langgraph.graph import StateGraph, START, END

from graph.state import AgentState

from agents.coordinator_agent import coordinator_agent
from agents.research_agent import research_agent
from agents.analyzer_agent import analyzer_agent
from agents.critic_agent import critic_agent
from agents.writer_agent import writer_agent


# ==========================================
# 1. CREATE LANGGRAPH WORKFLOW
# ==========================================

workflow = StateGraph(AgentState)


# ==========================================
# 2. REGISTER ALL FIVE AGENTS
# ==========================================

workflow.add_node("coordinator", coordinator_agent)
workflow.add_node("research", research_agent)
workflow.add_node("analyzer", analyzer_agent)
workflow.add_node("critic", critic_agent)
workflow.add_node("writer", writer_agent)


# ==========================================
# 3. DEFINE AGENT EXECUTION FLOW
# ==========================================

workflow.add_edge(START, "coordinator")

workflow.add_edge("coordinator", "research")

workflow.add_edge("research", "analyzer")

workflow.add_edge("analyzer", "critic")


# ==========================================
# 4. CONDITIONAL ROUTING AFTER CRITIC
# ==========================================

def critic_decision(state):

    # Stop if analysis is empty
    if not state.get("analysis", "").strip():

        print("\n[Workflow] Analysis is empty.")
        print("[Workflow] Stopping execution.")

        return "end"

    # If approved, send to Writer
    if state.get("approved", False):

        print("\n[Workflow] Analysis approved.")
        print("[Workflow] Sending to Writer.")

        return "writer"

    # Retry Analyzer if attempts remain
    if state.get("retry_count", 0) < 2:

        print("\n[Workflow] Analysis rejected.")
        print("[Workflow] Retrying Analyzer.")

        return "analyzer"

    # Stop after maximum retries
    print("\n[Workflow] Maximum retry limit reached.")

    return "end"


workflow.add_conditional_edges(
    "critic",
    critic_decision,
    {
        "writer": "writer",
        "analyzer": "analyzer",
        "end": END
    }
)


# ==========================================
# 5. WRITER COMPLETES THE WORKFLOW
# ==========================================

workflow.add_edge("writer", END)


# ==========================================
# 6. COMPILE THE WORKFLOW
# ==========================================

multi_agent_app = workflow.compile()


print("Multi-Agent Workflow compiled successfully!")
