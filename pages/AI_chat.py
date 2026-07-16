import streamlit as st
import pandas as pd

from backend.chatbot import ask_crime_ai

from components.theme import load_theme
from components.officer_panel import officer_panel
from components.quick_actions import quick_actions
from components.chat_window import chat_window
from components.ai_suggestions import ai_suggestions
from components.voice_input import voice_input

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------

st.set_page_config(
    page_title="AI Crime Assistant",
    page_icon="🛡",
    layout="wide"
)
st.markdown("""
<style>

/* Reduce chat input width */
[data-testid="stChatInput"]{
    max-width: 1000px;
    margin: auto;
}

</style>
""", unsafe_allow_html=True)
load_theme()

# ----------------------------------------------------
# LOAD DATA
# ----------------------------------------------------

df = pd.read_csv("data/crime.csv")

# ----------------------------------------------------
# HEADER
# ----------------------------------------------------

st.markdown("""
<div style="
background:linear-gradient(90deg,#0B2948,#0F4C75);
padding:20px;
border-radius:15px;
margin-bottom:20px;
">

<h1 style="color:white;">
🛡 KSP Crime Intelligence Platform
</h1>

<p style="color:#CFE9FF;">
AI Powered Crime Investigation & Analytics
</p>

</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# LAYOUT
# ----------------------------------------------------
left, center = st.columns([1, 3])

# ====================================================
# LEFT PANEL
# ====================================================

with left:

    officer_panel(df)

    st.divider()

    quick_actions()

    st.divider()

    ai_suggestions()


# ====================================================
# CENTER PANEL
# ====================================================

with center:

    chat_window()



# ====================================================
# VOICE ASSISTANT
# ====================================================

voice_query = voice_input()

if voice_query:

    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.session_state.messages.append(
        {
            "role": "user",
            "content": voice_query
        }
    )

    answer = ask_crime_ai(voice_query)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    st.rerun()