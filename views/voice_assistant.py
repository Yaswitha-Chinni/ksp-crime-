import streamlit as st

from backend.chatbot import ask_crime_ai
from components.voice_input import voice_input

st.title("🎤 KSP Voice Crime Assistant")

question = voice_input()

if question:

    st.success(f"👮 Officer: {question}")

    with st.spinner("🤖 Crime AI is analyzing..."):

        answer = ask_crime_ai(question)

    st.markdown("## 🤖 AI Response")

    st.write(answer)