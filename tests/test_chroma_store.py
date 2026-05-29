from memory.chroma_store import save_to_memory, get_learning_history, search_similar_topics


def test_chroma_memory_saves_learning_session():
    result = save_to_memory("test_student", "Python loops", "beginner")

    assert result["status"] == "saved"
    assert result["topic"] == "Python loops"


def test_chroma_memory_gets_learning_history():
    save_to_memory("history_student", "Python functions", "intermediate")

    history = get_learning_history("history_student")

    assert history is not None
    assert len(history["documents"]) >= 1


def test_chroma_memory_finds_similar_topic():
    save_to_memory("similar_student", "Python loops", "beginner")

    result = search_similar_topics("Python iteration", "similar_student")

    assert result is not None
    assert len(result["documents"][0]) >= 1