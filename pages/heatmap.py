import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Crime Heatmap",
    page_icon="🗺️",
    layout="wide"
)

st.title("🗺️ Karnataka Crime Heatmap")

# Load dataset
df = pd.read_csv("data/crime.csv")

# Check required columns
required_columns = ["Latitude", "Longitude", "Crime_Type", "District"]

missing = [col for col in required_columns if col not in df.columns]

if missing:
    st.error(f"Missing columns in dataset: {missing}")
    st.stop()

# Create map centered on Karnataka
crime_map = folium.Map(
    location=[15.3173, 75.7139],
    zoom_start=7
)

# Add markers
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=5,
        popup=f"""
        <b>Crime:</b> {row['Crime_Type']}<br>
        <b>District:</b> {row['District']}
        """,
        color="red",
        fill=True,
        fill_opacity=0.7
    ).add_to(crime_map)

st_folium(crime_map, width=1200, height=600)