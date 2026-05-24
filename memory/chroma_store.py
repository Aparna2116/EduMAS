import chromadb
from datetime import datetime

# Persistent database folder
client = chromadb.PersistentClient(path="./data/chroma_db")


def get_collection():

    collection = client.get_or_create_collection(
        name="student_memory"
    )

    return collection


def save_to_memory(student_id, topic, level):

    collection = get_collection()

    document_id = f"{student_id}_{datetime.now().strftime('%Y%m%d%H%M%S')}"

    collection.add(
        documents=[
            f"Student studied {topic} at {level} level"
        ],
        metadatas=[
            {
                "student_id": student_id,
                "topic": topic,
                "level": level,
                "timestamp": datetime.now().isoformat()
            }
        ],
        ids=[document_id]
    )

    return {
        "status": "saved",
        "topic": topic
    }


def get_learning_history(student_id):

    collection = get_collection()

    results = collection.get(
        where={"student_id": student_id}
    )

    return results


def search_similar_topics(query, student_id):

    collection = get_collection()

    results = collection.query(
        query_texts=[query],
        n_results=3,
        where={"student_id": student_id}
    )

    return results


if __name__ == "__main__":

    save_to_memory(
        "aparna",
        "Python loops",
        "beginner"
    )

    save_to_memory(
        "aparna",
        "Python functions",
        "intermediate"
    )

    history = get_learning_history("aparna")

    print("\nLEARNING HISTORY:\n")
    print(history)

    similar = search_similar_topics(
        "Python iteration",
        "aparna"
    )

    print("\nSIMILAR TOPICS:\n")
    print(similar)