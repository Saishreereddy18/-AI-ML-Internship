from typing import TypedDict, List
from langgraph.graph import StateGraph, START, END


# 1. Company documents used by the retriever
DOCUMENTS = [
    "Employees receive 20 paid leaves per year.",
    "Employees can work from home 2 days per week.",
    "New employee onboarding takes 5 working days.",
    "Multi-factor authentication (MFA) is required for company accounts.",
    "Employees receive certificates after completing approved training."
]


# 2. Define the shared workflow state
class WorkflowState(TypedDict):
    question: str
    documents: List[str]
    context: str
    answer: str
    memory: List[str]
    error: str


# 3. Node: receive the question
def receive_question(state: WorkflowState):
    print("\n[Node] Receiving question")

    return {
        "question": state["question"],
        "documents": [],
        "context": "",
        "answer": "",
        "error": ""
    }


# 4. Node: retrieve relevant documents
def retrieve_documents(state: WorkflowState):
    print("[Node] Retrieving documents")

    question = state["question"].lower()

    # Simulate a retrieval failure for testing
    if "[fail]" in question:
        return {
            "documents": [],
            "context": "",
            "error": "Simulated retriever failure"
        }

    keywords = [
        word.strip("?!.,") for word in question.split()
        if len(word) > 2
    ]

    matches = [
        doc for doc in DOCUMENTS
        if any(word in doc.lower() for word in keywords)
    ]

    return {
        "documents": matches,
        "context": "\n".join(matches),
        "error": ""
    }


# 5. Conditional routing after retrieval
def route_after_retrieval(state: WorkflowState):
    if state.get("error"):
        return "recover"

    if not state.get("documents"):
        return "no_context"

    return "generate"


# 6. Node: generate an answer from retrieved context
def generate_answer(state: WorkflowState):
    print("[Node] Generating answer")

    return {
        "answer": (
            "Based on the company documents:\n"
            + state["context"]
        ),
        "error": ""
    }


# 7. Node: recover when retrieval fails
def recover_from_error(state: WorkflowState):
    print("[Node] Recovering from retrieval failure")

    return {
        "answer": (
            "The document retriever failed. "
            "Please retry your question or check the document source."
        ),
        "error": state.get("error", "")
    }


# 8. Node: handle questions with no matching documents
def no_context_found(state: WorkflowState):
    print("[Node] No relevant context found")

    return {
        "answer": (
            "I couldn't find relevant information in the company "
            "documents. Please rephrase your question."
        )
    }


# 9. Node: save the conversation in memory
def save_memory(state: WorkflowState):
    print("[Node] Saving conversation to memory")

    previous_memory = state.get("memory", [])
    conversation = (
        f"Question: {state['question']}\n"
        f"Answer: {state['answer']}"
    )

    return {"memory": previous_memory + [conversation]}


# 10. Create the graph
builder = StateGraph(WorkflowState)

builder.add_node("receive", receive_question)
builder.add_node("retrieve", retrieve_documents)
builder.add_node("generate", generate_answer)
builder.add_node("recover", recover_from_error)
builder.add_node("no_context", no_context_found)
builder.add_node("save_memory", save_memory)

# Normal workflow
builder.add_edge(START, "receive")
builder.add_edge("receive", "retrieve")

# Conditional routing
builder.add_conditional_edges(
    "retrieve",
    route_after_retrieval,
    {
        "generate": "generate",
        "recover": "recover",
        "no_context": "no_context"
    }
)

# All paths save the conversation
builder.add_edge("generate", "save_memory")
builder.add_edge("recover", "save_memory")
builder.add_edge("no_context", "save_memory")

builder.add_edge("save_memory", END)

app = builder.compile()


# 11. Run the workflow and preserve state between questions
if __name__ == "__main__":
    conversation_memory = []

    print("LANGGRAPH COMPANY QUESTION ANSWERING SYSTEM")
    print("Type 'exit' to stop.")
    print("Type '[fail]' in a question to test error recovery.\n")

    while True:
        question = input("You: ").strip()

        if question.lower() == "exit":
            break

        if not question:
            print("Please enter a question.\n")
            continue

        initial_state = {
            "question": question,
            "documents": [],
            "context": "",
            "answer": "",
            "memory": conversation_memory,
            "error": ""
        }

        try:
            result = app.invoke(initial_state)
            conversation_memory = result.get("memory", [])

            print("\nAnswer:", result["answer"])
            print("Memory entries:", len(conversation_memory))
            print("-" * 50)

        except Exception as exc:
            print("Unexpected workflow error:", exc)
            print("Please retry the question.\n")