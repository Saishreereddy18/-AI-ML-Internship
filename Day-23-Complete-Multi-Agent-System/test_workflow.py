
from graph.workflow import multi_agent_app

print("\nTesting LangGraph Workflow")

print("Workflow compiled successfully!")

print("\nRegistered Agents:")

for node in multi_agent_app.get_graph().nodes:
    print("-", node)
