import streamlit as st

def officer_panel(df):

    st.markdown("""
    <div style="
    background:#102542;
    padding:20px;
    border-radius:15px;
    border:1px solid cyan;
    ">

    <h2>👮 Officer</h2>

    <hr>

    <b>Name</b><br>

    Inspector Rahul<br><br>

    <b>Badge</b><br>

    KSP-1025<br><br>

    <b>Status</b><br>

    🟢 Online<br><br>

    <b>Role</b><br>

    Crime Investigation

    </div>
    """,unsafe_allow_html=True)

    st.write("")

    st.metric("🚔 Total Crimes",len(df))
    st.metric("🏙 Districts",df["District"].nunique())
    st.metric("👮 Stations", df["Police_Station"].nunique())
    st.metric("📂 Crime Types",df["Crime_Type"].nunique())