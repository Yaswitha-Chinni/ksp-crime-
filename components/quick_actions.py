import streamlit as st

def quick_actions():

    st.subheader("⚡ Quick Actions")

    if st.button("🚔 Theft Cases", key="quick_theft"):
        st.session_state.quick = "Show theft cases"

    if st.button("🔴 Murder Cases", key="quick_murder"):
        st.session_state.quick = "Show murder cases"

    if st.button("💻 Cyber Crimes", key="quick_cyber"):
        st.session_state.quick = "Show cyber crime report"

    if st.button("📍 Highest Crime District", key="quick_district"):
        st.session_state.quick = "Highest crime district"

    if st.button("🔪 Weapon Analysis", key="quick_weapon"):
        st.session_state.quick = "Weapon analysis"