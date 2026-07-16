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

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("data/crime.csv")

# ==================================================
# ADD THE FILTERS HERE
# ==================================================

# District Filter
col1, col2 = st.columns(2)

with col1:
    district = st.selectbox(
        "📍 Select District",
        ["All"] + sorted(df["District"].unique())
    )

with col2:
    crime = st.selectbox(
        "🚔 Crime Type",
        ["All"] + sorted(df["Crime_Type"].unique())
    )

if district != "All":
    df = df[df["District"] == district]

if crime != "All":
    df = df[df["Crime_Type"] == crime]
# ==================================================
# CREATE MAP
# ==================================================

m = folium.Map(
    location=[15.3173, 75.7139],
    zoom_start=7
)

# ==================================================
# ADD MARKERS
# ==================================================

for _, row in df.iterrows():

    color = "green"

    if row["Severity"] == "Medium":
        color = "orange"

    elif row["Severity"] == "High":
        color = "red"

    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=6,
        popup=f"""
        FIR : {row['FIR_No']}<br>
        Crime : {row['Crime_Type']}<br>
        District : {row['District']}<br>
        Police Station : {row['Police_Station']}<br>
        Severity : {row['Severity']}
        """,
        color=color,
        fill=True,
        fill_color=color
    ).add_to(m)

# ==================================================
# SHOW MAP
# ==================================================

try:
    st_folium(
        m,
        width=1200,
        height=700
    )
except Exception as e:
    st.exception(e)
df = pd.read_csv("data/crime.csv")
st.write(df.columns.tolist())
st.write(df[["Latitude", "Longitude"]].head())