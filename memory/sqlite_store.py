import sqlite3
from datetime import datetime

DB_PATH = "./data/edumas.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            level TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            topic TEXT NOT NULL,
            score REAL DEFAULT 0,
            created_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def create_student(student_id: str, name: str, level: str):
    init_db()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT OR IGNORE INTO students (id, name, level, created_at)
        VALUES (?, ?, ?, ?)
        """,
        (student_id, name, level, datetime.now().isoformat())
    )

    conn.commit()
    conn.close()

    return {
        "status": "student_created",
        "student_id": student_id,
        "name": name,
        "level": level
    }


def get_student(student_id: str):
    init_db()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, name, level, created_at FROM students WHERE id = ?",
        (student_id,)
    )

    row = cursor.fetchone()
    conn.close()

    if row is None:
        return None

    return {
        "student_id": row[0],
        "name": row[1],
        "level": row[2],
        "created_at": row[3]
    }


def log_session(student_id: str, topic: str, score: float = 0.0):
    init_db()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO sessions (student_id, topic, score, created_at)
        VALUES (?, ?, ?, ?)
        """,
        (student_id, topic, score, datetime.now().isoformat())
    )

    conn.commit()
    conn.close()

    return {
        "status": "session_logged",
        "student_id": student_id,
        "topic": topic,
        "score": score
    }


def get_sessions(student_id: str):
    init_db()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT topic, score, created_at
        FROM sessions
        WHERE student_id = ?
        ORDER BY created_at DESC
        """,
        (student_id,)
    )

    rows = cursor.fetchall()
    conn.close()

    sessions = []

    for row in rows:
        sessions.append({
            "topic": row[0],
            "score": row[1],
            "created_at": row[2]
        })

    return sessions


if __name__ == "__main__":
    print(create_student("aparna", "Aparna", "beginner"))
    print(get_student("aparna"))
    print(log_session("aparna", "Python dictionaries", 0.0))
    print(get_sessions("aparna"))