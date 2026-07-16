import streamlit as st

def investigation_tools():

    st.subheader("🛠 Investigation Tools")

    st.markdown("### 🎤 Voice Assistant")

    st.button(
        "🎤 Start Voice",
        key="voice_start"
    )

    st.divider()

    st.markdown("### 📎 FIR Upload")

    st.file_uploader(
        "Upload FIR PDF",
        type=["pdf"],
        key="fir_upload"
    )

    st.divider()

    st.markdown("### 📄 Reports")

    st.button(
        "📄 Export Investigation Report",
        key="export_pdf"
    )