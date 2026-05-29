from tools.llm import get_llm
import json


def generate_quiz(topic: str, level: str):

    llm = get_llm()

    prompt = f"""
You are a quiz generation agent for EduMAS.

Create exactly 5 multiple-choice questions for this topic:
Topic: {topic}
Level: {level}

Rules:
- Each question must have 4 meaningful options: A, B, C, D
- Do NOT write "Option A", "Option B", etc.
- Do NOT reveal the correct answer inside the student_quiz
- Do NOT include explanations inside the student_quiz
- Return ONLY valid JSON
- No markdown outside JSON

Use this exact JSON format:

{{
  "student_quiz": "Question 1\\n...\\nA. ...\\nB. ...\\nC. ...\\nD. ...\\n\\nQuestion 2\\n...",
  "answer_key": {{
    "q1": "A",
    "q2": "B",
    "q3": "C",
    "q4": "D",
    "q5": "A"
  }}
}}
"""

    response = llm.invoke(prompt)
    raw = response.content if hasattr(response, "content") else str(response)

    try:
        clean = raw.strip().replace("```json", "").replace("```", "")
        quiz_data = json.loads(clean)

        return {
            "student_quiz": quiz_data["student_quiz"],
            "answer_key": quiz_data["answer_key"]
        }

    except Exception:
        return {
            "student_quiz": f"""
Question 1
What is the purpose of {topic}?

A. To repeat or understand the main concept
B. To delete data
C. To shut down the program
D. To ignore instructions

Question 2
Which option is related to {topic}?

A. A random image
B. A relevant programming or learning concept
C. A computer virus
D. A file name only

Question 3
Why is {topic} useful?

A. It makes learning harder
B. It has no use
C. It helps solve problems efficiently
D. It stops execution

Question 4
Which is a good practice when learning {topic}?

A. Memorize without practice
B. Avoid examples
C. Skip basics
D. Practice with examples

Question 5
What should a beginner do first with {topic}?

A. Learn the basic idea
B. Ignore syntax
C. Start with advanced errors
D. Avoid practice
""",
            "answer_key": {
                "q1": "A",
                "q2": "B",
                "q3": "C",
                "q4": "D",
                "q5": "A"
            }
        }