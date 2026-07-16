import streamlit as st

st.set_page_config(
    page_title="FIR Upload",
    page_icon="📎",
    layout="wide"
)

st.title("📎 FIR Upload")

uploaded = st.file_uploader(
    "Upload FIR",
    type=["pdf"]
)

if uploaded:
    st.success("FIR Uploaded Successfully")