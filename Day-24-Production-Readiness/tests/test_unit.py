
import pytest

from agents.analyzer_agent import analyzer_agent
from graph.career_workflow import career_critic_decision


def test_analyzer_with_valid_data():
    state = {
        "research_data": "AI and Machine Learning job opportunities",
        "errors": []
    }

    result = analyzer_agent(state)

    assert result["analysis"] != ""
    assert result["current_agent"] == "analyzer"


def test_analyzer_with_empty_data():
    state = {
        "research_data": "",
        "errors": []
    }

    result = analyzer_agent(state)

    assert result["analysis"] == ""
    assert len(result["errors"]) == 1


def test_critic_approved():
    state = {
        "analysis": "Valid analysis",
        "approved": True
    }

    assert career_critic_decision(state) == "writer"


def test_critic_retry():
    state = {
        "analysis": "Valid analysis",
        "approved": False,
        "retry_count": 0
    }

    assert career_critic_decision(state) == "analyzer"


def test_critic_retry_limit():
    state = {
        "analysis": "Valid analysis",
        "approved": False,
        "retry_count": 2
    }

    assert career_critic_decision(state) == "end"
