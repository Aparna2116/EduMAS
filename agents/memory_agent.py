from memory.chroma_store import (
    save_to_memory,
    get_learning_history,
    search_similar_topics
)


def remember_learning_session(student_id: str, topic: str, level: str):
    result = save_to_memory(student_id, topic, level)
    return result


def recall_learning_history(student_id: str):
    history = get_learning_history(student_id)

    metadatas = history.get("metadatas", [])

    clean_history = []

    for item in metadatas:
        clean_history.append({
            "topic": item.get("topic"),
            "level": item.get("level"),
            "timestamp": item.get("timestamp")
        })

    return clean_history


def recall_similar_learning(query: str, student_id: str):
    similar_topics = search_similar_topics(query, student_id)

    metadatas = similar_topics.get("metadatas", [[]])[0]

    clean_similar = []

    for item in metadatas:
        clean_similar.append({
            "topic": item.get("topic"),
            "level": item.get("level"),
            "timestamp": item.get("timestamp")
        })

    return clean_similar