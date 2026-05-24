from fastapi import FastAPI
from httpcore import request
from pydantic import BaseModel

from agents.curriculum_agent import generate_curriculum
from agents.quiz_agent import generate_quiz
from agents.memory_agent import save_to_memory, get_learning_history

app = FastAPI()


class LessonRequest(BaseModel):
    topic: str
    level: str


@app.get("/")
def home():
    return {"message": "EduMAS backend is running successfully"}


@app.post("/lesson")
def generate_lesson(request: LessonRequest):

    lesson = generate_curriculum(
        request.topic,
        request.level
    )

    quiz = generate_quiz(
        request.topic,
        request.level
   )
    save_to_memory(
        request.topic,
        request.level
  )

    history = get_learning_history()

    return {
        "status": "success",
        "topic": request.topic,
        "level": request.level,
        "lesson": lesson,
        "quiz": quiz,
        "learning_history": history
   }