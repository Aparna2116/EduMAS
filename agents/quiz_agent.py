from tools.llm import client


def generate_quiz(topic: str, level: str):

    prompt = f"""
    You are an expert educational quiz creator.

    Generate exactly 5 multiple choice questions.

    Topic: {topic}
    Difficulty Level: {level}

    Requirements:
    - Each question must have 4 options:
    A, B, C, D
    - Clearly mention the correct answer
    - Add a short explanation after each answer
    - Keep questions beginner friendly
    - Format cleanly using markdown

    Example format:

    ## Question 1
    What is Python?

    A. Database
    B. Programming Language
    C. Browser
    D. Hardware

    Correct Answer: B

    Explanation:
    Python is a programming language.

    Repeat this structure for all questions.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    quiz = response.choices[0].message.content

    return quiz