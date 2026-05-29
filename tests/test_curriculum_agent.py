from agents.curriculum_agent import generate_curriculum


def test_generate_curriculum_returns_lesson():

    lesson = generate_curriculum("Python loops", "beginner")

    assert lesson is not None
    assert len(lesson) > 50

    lesson_lower = lesson.lower()

    assert "python" in lesson_lower
    assert "loop" in lesson_lower
    assert "beginner" in lesson_lower