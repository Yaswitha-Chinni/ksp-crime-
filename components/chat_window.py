import streamlit as st
from backend.chatbot import ask_crime_ai


def chat_window():

    # -----------------------
    # AI Status
    # -----------------------

    st.subheader("🤖 AI Crime Assistant")
    st.success("🟢 Crime AI Online")

    # -----------------------
    # Session State
    # -----------------------

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # -----------------------
    # Handle Quick Actions
    # -----------------------

    if "quick" in st.session_state:

        prompt = st.session_state.pop("quick")

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.spinner("🤖 Crime AI is analyzing the database..."):

            answer = ask_crime_ai(prompt)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        st.rerun()

    # -----------------------
    # Display Chat History
    # -----------------------

    for message in st.session_state.messages:

        avatar = "👮" if message["role"] == "user" else "🤖"

        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

    # -----------------------
    # Chat Input
    # -----------------------

    input_col1, input_col2 = st.columns([6, 1])

    with input_col1:
        prompt = st.chat_input("Ask about Karnataka crime...")

    if prompt:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user", avatar="👮"):
            st.markdown(prompt)

        with st.chat_message("assistant", avatar="🤖"):

            with st.spinner("🤖 Crime AI is analyzing the database..."):

                answer = ask_crime_ai(prompt)

                st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        st.rerun()