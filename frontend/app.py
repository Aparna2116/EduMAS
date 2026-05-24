import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="EduMAS",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 EduMAS")
st.subheader("AI-Powered Multi-Agent Learning System")

st.markdown("---")

student_id = st.text_input(
    "Student ID",
    value="aparna"
)

topic = st.text_input(
    "Enter a topic to learn"
)

level = st.selectbox(
    "Select difficulty level",
    ["beginner", "intermediate", "advanced"]
)

if st.button("Generate Lesson"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:

        payload = {
            "topic": topic,
            "level": level,
            "student_id": student_id
        }

        with st.spinner("Generating lesson..."):

            response = requests.post(
                f"{API_URL}/lesson",
                json=payload
            )

        if response.status_code == 200:

            data = response.json()

            st.success("Lesson generated successfully!")

            st.markdown("## 📘 Lesson")
            st.markdown(data["lesson"])

            st.markdown("---")
            st.markdown("## 📝 Quiz")
            st.markdown(data["quiz"])

            st.markdown("### 🧠 Memory Status")
            st.json(data.get("memory", {}))

            st.markdown("### 🗂️ Session Status")
            st.json(data.get("session", {}))

        else:
            st.error("Failed to generate lesson.")


st.markdown("---")
st.markdown("## 📚 Learning History")

if st.button("Load Learning History"):

    history_response = requests.get(
        f"{API_URL}/history/{student_id}"
    )

    if history_response.status_code == 200:

        history_data = history_response.json()
        history = history_data.get("learning_history", [])

        if len(history) == 0:
            st.info("No learning history found.")
        else:
            for item in history:
                st.write(
                    f"📌 {item['topic']} — {item['level']} — {item['timestamp']}"
                )

    else:
        st.error("Failed to load learning history.")

st.markdown("---")
st.markdown("## 🔍 Similar Topics Search")

search_query = st.text_input(
    "Search related topics"
)

if st.button("Find Similar Topics"):

    if search_query.strip() == "":
        st.warning("Please enter a search query.")

    else:

        similar_response = requests.get(
            f"{API_URL}/similar/{student_id}",
            params={"query": search_query}
        )

        if similar_response.status_code == 200:

            similar_data = similar_response.json()

            similar_topics = similar_data.get(
                "similar_topics",
                []
            )

            if len(similar_topics) == 0:
                st.info("No similar topics found.")

            else:

                st.success("Similar topics found!")

                for item in similar_topics:

                    st.write(
                        f"📘 {item['topic']} — {item['level']}"
                    )

        else:
            st.error("Failed to search similar topics.")