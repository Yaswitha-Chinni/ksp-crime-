import streamlit as st
import plotly.express as px

def crime_chart(df):

    crime = (
        df.groupby("Crime_Type")
        .size()
        .reset_index(name="Cases")
    )

    fig = px.bar(
        crime,
        x="Crime_Type",
        y="Cases",
        color="Cases",
        title="Crime Categories"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
def severity_chart(df):

    fig = px.pie(
        df,
        names="Severity",
        title="Crime Severity"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )