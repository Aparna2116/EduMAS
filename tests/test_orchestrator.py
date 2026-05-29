from agents.orchestrator import workflow


def test_full_workflow():

    initial_state = {
        "student_id": "aparna",
        "topic": "Python loops",
        "level": "beginner"
    }

    result = workflow.invoke(initial_state)

    assert "lesson" in result
    assert "quiz" in result
    assert "adaptive_result" in result
    assert "memory_result" in result
    assert "session_result" in result