from fastapi import FastAPI
from httpcore import request
from pydantic import BaseModel

from agents.orchestrator import workflow
from agents.curriculum_agent import generate_curriculum
from agents.quiz_agent import generate_quiz
from agents.memory_agent import save_to_memory, get_learning_history
from agents.scoring_agent import evaluate_quiz
from memory.sqlite_store import log_session
from agents.adaptive_agent import determine_next_level
from agents.orchestrator import workflow

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

class ScoreRequest(BaseModel):
    student_id: str
    topic: str
    correct_answers: dict
    student_answers: dict

class AdaptiveRequest(BaseModel):
    student_id: str
    current_level: str

@app.get("/")
def home():
    return {"message": "EduMAS backend is running successfully"}


@app.post("/lesson")
def generate_lesson(request: LessonRequest):

    initial_state = {
        "student_id": "aparna",
        "topic": request.topic,
        "level": request.level
    }

    result = workflow.invoke(initial_state)

    return {
        "status": "success",
        "adaptive_result": result.get("adaptive_result"),
        "lesson": result.get("lesson"),
        "quiz": result.get("quiz"),
        "answer_key": result.get("answer_key"),
        "memory_result": result.get("memory_result"),
        "session_result": result.get("session_result")
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

@app.post("/score")
def score_quiz(request: ScoreRequest):

    result = evaluate_quiz(
        request.correct_answers,
        request.student_answers
    )

    log_session(
        student_id=request.student_id,
        topic=request.topic,
        score=result["score_percent"]
    )

    return {
        "status": "success",
        "score_result": result,
        "message": "Score saved to SQLite"
    }

@app.post("/adaptive-level")
def adaptive_level(request: AdaptiveRequest):

    result = determine_next_level(
        student_id=request.student_id,
        current_level=request.current_level
    )

    return {
        "status": "success",
        "adaptive_result": result
    }