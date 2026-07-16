import streamlit as st

def ai_suggestions():

    st.subheader("💡 AI Suggestions")

    if st.button("🚔 Theft Cases", key="s1"):
        st.session_state.quick = "Show theft cases"

    if st.button("🔪 Murder Report", key="s2"):
        st.session_state.quick = "Show murder report"

    if st.button("💻 Cyber Crimes", key="s3"):
        st.session_state.quick = "Show cyber crime report"

    if st.button("📍 Crime Hotspots", key="s4"):
        st.session_state.quick = "Highest crime district"

    if st.button("🔫 Weapon Analysis", key="s5"):
        st.session_state.quick = "Weapon analysis"

    if st.button("⚠ High Severity", key="s6"):
        st.session_state.quick = "Show high severity crimes"