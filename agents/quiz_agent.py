from tools.llm import client


def generate_quiz(topic: str, level: str):

    prompt = f"""
    You are an expert educational quiz creator.

    Generate 5 multiple choice questions for:

    Topic: {topic}
    Difficulty Level: {level}

    Rules:
    - Each question must have 4 options
    - Clearly mention the correct answer
    - Keep questions beginner friendly
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