from agents.adaptive_agent import determine_next_level


def test_adaptive_agent_returns_valid_response():

    result = determine_next_level(
        student_id="aparna",
        current_level="beginner"
    )

    assert "recommended_level" in result
    assert "reason" in result