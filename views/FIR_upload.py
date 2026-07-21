import streamlit as st



st.title("📎 FIR Upload")

uploaded = st.file_uploader(
    "Upload FIR",
    type=["pdf"]
)

if uploaded:
    st.success("FIR Uploaded Successfully")