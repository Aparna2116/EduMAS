from tools.llm import client


def generate_curriculum(topic: str, level: str):

    prompt = f"""
    You are an expert educational teacher.

    Generate a detailed educational lesson.

    Topic: {topic}

    Difficulty Level: {level}

    The lesson should include:
    1. Introduction
    2. Core Concepts
    3. Easy Examples
    4. Summary

    Keep the lesson beginner friendly and structured properly.
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

    lesson = response.choices[0].message.content

    return lesson