from agents.scoring_agent import evaluate_quiz


def test_quiz_scoring():

    correct_answers = {
        "q1": "A",
        "q2": "B",
        "q3": "C"
    }

    student_answers = {
        "q1": "A",
        "q2": "B",
        "q3": "D"
    }

    result = evaluate_quiz(
        correct_answers,
        student_answers
    )

    assert result["score"] == 2
    assert result["score_percent"] == (2 / 3) * 100