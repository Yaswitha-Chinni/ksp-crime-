import streamlit as st
from pypdf import PdfReader

def fir_upload():

    uploaded = st.file_uploader(
        "📎 Upload FIR (PDF)",
        type=["pdf"]
    )

    if uploaded is not None:

        reader = PdfReader(uploaded)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

        st.success("✅ FIR Uploaded Successfully")

        return text

    return None