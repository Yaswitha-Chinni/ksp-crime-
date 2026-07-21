import streamlit as st



st.title("📄 Export Investigation Report")

st.write("Generate and download AI investigation reports.")

if st.button("Generate Report"):
    st.success("Report generated successfully!")

if st.button("Download PDF"):
    st.info("PDF download functionality will be added next.")