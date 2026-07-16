import streamlit as st

def top_cards(df):

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "🚔 Total Crimes",
            len(df)
        )

    with c2:
        st.metric(
            "🏙 Districts",
            df["District"].nunique()
        )

    with c3:
        st.metric(
            "👮 Police Stations",
            df["Police_Station"].nunique()
        )

    with c4:
        high = len(df[df["Severity"] == "High"])

        st.metric(
            "🚨 High Severity",
            high
        )