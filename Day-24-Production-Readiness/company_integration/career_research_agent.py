
def career_research_agent(state):

    print("\n[Career Research Agent]")
    print("Processing AI Career Copilot job results...")

    # Receive job results from AI Career Copilot
    job_results = state.get("job_results", [])

    if not job_results:

        error_message = "No job results received from AI Career Copilot."

        print("Error:", error_message)

        return {
            "research_data": "",
            "current_agent": "career_research",
            "errors": state.get("errors", []) + [
                error_message
            ]
        }

    # Prepare job information
    research_summary = []

    for index, job in enumerate(job_results, start=1):

        title = job.get("title", "Not provided")
        company = job.get("company", "Not provided")
        location = job.get("location", "Not provided")

        skills = (
            job.get("required_skills")
            or job.get("skills")
            or []
        )

        description = job.get("description", "Not provided")
        source = job.get("source", "Not provided")
        url = job.get("url", "Not provided")

        if isinstance(skills, list):
            skills = ", ".join(str(skill) for skill in skills)

        research_summary.append(
            f"""
Job {index}
---------
Job Title: {title}
Company: {company}
Location: {location}
Required Skills: {skills}
Description: {description}
Source: {source}
Job URL: {url}
"""
        )

    research_data = "\n".join(research_summary)

    print("Job research completed.")
    print("Jobs Processed:", len(job_results))

    return {
        "research_data": research_data,
        "current_agent": "career_research"
    }
