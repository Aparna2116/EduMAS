import json


MEMORY_FILE = "memory/student_memory.json"


def save_to_memory(topic, level):

    with open(MEMORY_FILE, "r") as file:
        data = json.load(file)

    data["history"].append({
        "topic": topic,
        "level": level
    })

    with open(MEMORY_FILE, "w") as file:
        json.dump(data, file, indent=4)


def get_learning_history():

    with open(MEMORY_FILE, "r") as file:
        data = json.load(file)

    return data["history"]