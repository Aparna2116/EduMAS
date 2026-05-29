def evaluate_quiz(correct_answers: dict, student_answers: dict):

    total_questions = len(correct_answers)
    correct_count = 0

    results = {}

    for question, correct_answer in correct_answers.items():

        student_answer = student_answers.get(question)

        is_correct = student_answer == correct_answer

        if is_correct:
            correct_count += 1

        results[question] = {
            "student_answer": student_answer,
            "correct_answer": correct_answer,
            "is_correct": is_correct
        }

    score_percent = (correct_count / total_questions) * 100

    return {
        "results": results,
        "score": correct_count,
        "total_questions": total_questions,
        "score_percent": score_percent
    }