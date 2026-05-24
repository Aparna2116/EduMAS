from fastapi import FastAPI
from httpcore import request
from pydantic import BaseModel

from agents.orchestrator import workflow
from agents.curriculum_agent import generate_curriculum
from agents.quiz_agent import generate_quiz
from agents.memory_agent import save_to_memory, get_learning_history
from agents.memory_agent import (
    remember_learning_session,
    recall_learning_history,
    recall_similar_learning
)
from agents.student_agent import (
    register_student,
    fetch_student,
    save_session,
    fetch_sessions
)


app = FastAPI()


class LessonRequest(BaseModel):
    topic: str
    level: str
    student_id: str = "aparna"


@app.get("/")
def home():
    return {"message": "EduMAS backend is running successfully"}


@app.post("/lesson")
def generate_lesson(request: LessonRequest):

    result = workflow.invoke({
        "student_id": request.student_id,
        "topic": request.topic,
        "level": request.level
    })

    return {
        "status": "success",
        "topic": result["topic"],
        "level": result["level"],
        "student_id": result["student_id"],
        "lesson": result["lesson"],
        "quiz": result["quiz"],
        "memory": result["memory_result"],
        "session": result["session_result"]
    }

@app.get("/history/{student_id}")
def get_history(student_id: str):

    history = recall_learning_history(student_id)

    return {
        "student_id": student_id,
        "learning_history": history
    }

@app.get("/similar/{student_id}")
def get_similar_topics(student_id: str, query: str):

    similar = recall_similar_learning(query, student_id)

    return {
        "student_id": student_id,
        "query": query,
        "similar_topics": similar
    }

@app.post("/student/create")
def create_student_profile(
    student_id: str,
    name: str,
    level: str
):

    student = register_student(
        student_id,
        name,
        level
    )

    return student


@app.get("/student/{student_id}")
def get_student_profile(student_id: str):

    student = fetch_student(student_id)

    if student is None:
        return {
            "status": "not_found"
        }

    return student


@app.get("/sessions/{student_id}")
def get_student_sessions(student_id: str):

    sessions = fetch_sessions(student_id)

    return {
        "student_id": student_id,
        "sessions": sessions
    }