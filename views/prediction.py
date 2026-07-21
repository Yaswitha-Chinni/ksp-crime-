import streamlit as st



st.title("📈 Crime Prediction")

st.info("AI-based crime prediction module.")

district = st.selectbox(
    "Select District",
    [
        "Bengaluru Urban",
        "Mysuru",
        "Belagavi",
        "Dharwad"
    ]
)

crime = st.selectbox(
    "Crime Type",
    [
        "Theft",
        "Murder",
        "Cyber Crime"
    ]
)

if st.button("Predict"):

    st.success("Prediction Completed")

    st.metric(
        "Risk Level",
        "High"
    )

    st.write("Recommended Action:")

    st.write("• Increase police patrol")

    st.write("• Monitor hotspots")

    st.write("• Deploy cyber unit if required")