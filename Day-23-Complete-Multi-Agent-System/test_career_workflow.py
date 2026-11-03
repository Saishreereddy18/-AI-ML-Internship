
from graph.career_workflow import career_copilot_app


# ==========================================
# SAMPLE AI CAREER COPILOT JOB RESULTS
# ==========================================

sample_jobs = [
    {
        "title": "AI Engineer Intern",
        "company": "ABC Technologies",
        "location": "Hyderabad",
        "required_skills": [
            "Python",
            "Machine Learning",
            "LangChain",
            "RAG"
        ],
        "description": (
            "Work on AI-powered applications "
            "and intelligent automation systems."
        ),
        "source": "Sample Data",
        "url": "https://example.com/ai-engineer"
    },
    {
        "title": "Machine Learning Intern",
        "company": "XYZ Solutions",
        "location": "Remote",
        "required_skills": [
            "Python",
            "NumPy",
            "Pandas",
            "Scikit-learn"
        ],
        "description": (
            "Assist in building and evaluating "
            "machine learning models."
        ),
        "source": "Sample Data",
        "url": "https://example.com/ml-intern"
    }
]


# ==========================================
# INITIALIZE SHARED STATE
# ==========================================

initial_state = {
    "user_query": (
        "Analyze these AI and Machine Learning "
        "job opportunities."
    ),
    "job_results": sample_jobs,
    "research_data": "",
    "analysis": "",
    "critic_feedback": "",
    "final_answer": "",
    "current_agent": "coordinator",
    "errors": [],
    "retry_count": 0,
    "approved": False
}


# ==========================================
# EXECUTE CAREER COPILOT WORKFLOW
# ==========================================

print("\n===================================")
print(" AI CAREER COPILOT INTEGRATION TEST")
print("===================================")

try:

    result = career_copilot_app.invoke(initial_state)

    print("\n===================================")
    print(" CAREER COPILOT FINAL RESPONSE")
    print("===================================")

    print(result.get("final_answer", ""))

    print("\n===================================")
    print(" EXECUTION SUMMARY")
    print("===================================")

    print("Current Agent:", result["current_agent"])
    print("Jobs Processed:", len(sample_jobs))
    print("Approved:", result["approved"])
    print("Retry Count:", result["retry_count"])
    print("Errors:", result["errors"])

    if result.get("final_answer") and result["approved"]:
        print("\nCAREER WORKFLOW TEST PASSED!")

    else:
        print("\nCAREER WORKFLOW TEST NEEDS ATTENTION.")

except Exception as error:

    print("\nCAREER WORKFLOW ERROR:", str(error))
