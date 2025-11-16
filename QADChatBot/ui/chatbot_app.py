import streamlit as st
import requests

# Streamlit page configuration
st.set_page_config(page_title="RAG Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 QAD Chatbot")
st.write("Ask questions and get answers powered by Retrieval-Augmented Generation.")

API_URL = "http://127.0.0.1:8000/chat"  # FastAPI endpoint

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Bot:** {msg['content']}")

# Input box for user query
query = st.text_input("Enter your question:", "")

# Send query to FastAPI backend
if st.button("Send") and query.strip() != "":
    st.session_state["messages"].append({"role": "user", "content": query})
    try:
        response = requests.post(API_URL, json={"query": query})
        if response.status_code == 200:
            answer = response.json().get("answer", "No response")
        else:
            answer = f"Error: {response.status_code}"
    except Exception as e:
        answer = f"Request failed: {e}"

    st.session_state["messages"].append({"role": "bot", "content": answer})
    st.rerun()