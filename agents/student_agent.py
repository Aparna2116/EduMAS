from memory.sqlite_store import (
    create_student,
    get_student,
    log_session,
    get_sessions
)


def register_student(student_id: str, name: str, level: str):
    return create_student(student_id, name, level)


def fetch_student(student_id: str):
    return get_student(student_id)


def save_session(student_id: str, topic: str, score: float = 0.0):
    return log_session(student_id, topic, score)


def fetch_sessions(student_id: str):
    return get_sessions(student_id)