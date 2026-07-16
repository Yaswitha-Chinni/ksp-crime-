import streamlit as st
from streamlit_mic_recorder import speech_to_text


def voice_input():

    st.subheader("🎤 Voice Assistant")

    text = speech_to_text(
        language="en",
        start_prompt="🎤 Start Recording",
        stop_prompt="⏹ Stop Recording",
        just_once=True,
        use_container_width=True,
        key="voice_recorder"
    )

    return text