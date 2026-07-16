import streamlit as st
import plotly.express as px

def analytics(df):

    left,right=st.columns(2)

    with left:

        fig=px.bar(
            df.groupby("Crime_Type").size().reset_index(name="Cases"),
            x="Crime_Type",
            y="Cases",
            title="Crime Categories"
        )

        st.plotly_chart(fig,use_container_width=True)

    with right:

        fig=px.pie(
            df,
            names="District",
            title="District Crime Distribution"
        )

        st.plotly_chart(fig,use_container_width=True)