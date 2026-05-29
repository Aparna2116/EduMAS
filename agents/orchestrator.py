from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.curriculum_agent import generate_curriculum
from agents.quiz_agent import generate_quiz
from agents.memory_agent import remember_learning_session
from agents.student_agent import save_session
from agents.adaptive_agent import determine_next_level


class EduMASState(TypedDict):

    student_id: str
    topic: str
    level: str

    lesson: str
    quiz: str
    answer_key: dict

    memory_result: dict
    session_result: dict

    adaptive_result: dict


def adaptive_node(state: EduMASState):

    adaptive_result = determine_next_level(
        state["student_id"],
        state["level"]
    )

    state["adaptive_result"] = adaptive_result
    state["level"] = adaptive_result["recommended_level"]

    return state

def curriculum_node(state: EduMASState):

    lesson = generate_curriculum(
        state["topic"],
        state["level"]
    )

    state["lesson"] = lesson

    return state


def quiz_node(state: EduMASState):

    quiz_result = generate_quiz(
    state["topic"],
    state["level"]
)

    state["quiz"] = quiz_result["student_quiz"]
    state["answer_key"] = quiz_result["answer_key"]

    return state


def memory_node(state: EduMASState):

    memory_result = remember_learning_session(
        state["student_id"],
        state["topic"],
        state["level"]
    )

    state["memory_result"] = memory_result

    return state


def session_node(state: EduMASState):

    session_result = save_session(
        state["student_id"],
        state["topic"],
        0.0
    )

    state["session_result"] = session_result

    return state


graph = StateGraph(EduMASState)

graph.add_node(
    "adaptive_agent",
    adaptive_node
)

graph.add_node(
    "curriculum_agent",
    curriculum_node
)

graph.add_node(
    "quiz_agent",
    quiz_node
)

graph.add_node(
    "memory_agent",
    memory_node
)

graph.add_node(
    "student_agent",
    session_node
)

graph.set_entry_point("adaptive_agent")

graph.add_edge(
    "curriculum_agent",
    "quiz_agent"
)

graph.add_edge(
    "quiz_agent",
    "memory_agent"
)

graph.add_edge(
    "memory_agent",
    "student_agent"
)

graph.add_edge(
    "student_agent",
    END
)

graph.add_edge(
    "adaptive_agent",
    "curriculum_agent"
)

workflow = graph.compile()