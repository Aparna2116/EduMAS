import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="EduMAS", page_icon="🎓", layout="wide")

st.title("🎓 EduMAS")
st.subheader("Adaptive Multi-Agent Learning System")

if "lesson_data" not in st.session_state:
    st.session_state.lesson_data = None

student_id = st.text_input("Student ID", value="aparna")

topic = st.text_input(
    "Enter Topic",
    placeholder="Example: Python loops"
)

level = st.selectbox(
    "Select Level",
    ["beginner", "intermediate", "advanced"]
)

if st.button("Generate Lesson"):
    if not topic:
        st.warning("Please enter a topic first.")
    else:
        with st.spinner("AI Agents are working..."):
            response = requests.post(
                f"{API_URL}/lesson",
                json={
                    "topic": topic,
                    "level": level
                }
            )

        if response.status_code == 200:
            st.session_state.lesson_data = response.json()
            st.session_state.current_topic = topic
            st.success("Lesson Generated Successfully")
        else:
            st.error(response.text)

data = st.session_state.lesson_data

if data:

    st.markdown("## Adaptive Result")
    st.json(data["adaptive_result"])

    st.markdown("## Lesson")
    st.markdown(data["lesson"])

    st.markdown("## Quiz")
    st.markdown(data["quiz"])

    st.markdown("## Submit Answers")

    q1 = st.selectbox("Question 1", ["A", "B", "C", "D"], key="q1")
    q2 = st.selectbox("Question 2", ["A", "B", "C", "D"], key="q2")
    q3 = st.selectbox("Question 3", ["A", "B", "C", "D"], key="q3")
    q4 = st.selectbox("Question 4", ["A", "B", "C", "D"], key="q4")
    q5 = st.selectbox("Question 5", ["A", "B", "C", "D"], key="q5")

    if st.button("Submit Quiz"):
        score_response = requests.post(
            f"{API_URL}/score",
            json={
                "student_id": student_id,
                "topic": st.session_state.current_topic,
                "correct_answers": data["answer_key"],
                "student_answers": {
                    "q1": q1,
                    "q2": q2,
                    "q3": q3,
                    "q4": q4,
                    "q5": q5
                }
            }
        )

        if score_response.status_code == 200:
            score_data = score_response.json()

            st.markdown("## Quiz Result")
            st.json(score_data["score_result"])

            st.markdown("## Answer Key Used by System")
            st.json(data["answer_key"])

            st.success("Score saved to SQLite")
        else:
            st.error(score_response.text)

    st.markdown("## Memory Result")
    st.json(data["memory_result"])

    st.markdown("## Session Result")
    st.json(data["session_result"])