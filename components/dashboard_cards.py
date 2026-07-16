import streamlit as st

def dashboard_cards(df):

    total = len(df)

    districts = df["District"].nunique()

    stations = df["Police_Station"].nunique()

    crime_types = df["Crime_Type"].nunique()

    c1,c2,c3,c4=st.columns(4)

    c1.metric("🚔 Total Crimes",total)

    c2.metric("🏙 Districts",districts)

    c3.metric("👮 Stations",stations)

    c4.metric("📂 Crime Types",crime_types)