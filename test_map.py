import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Folium Test", layout="wide")

st.title("🗺️ Folium Test")

m = folium.Map(
    location=[12.9716, 77.5946],
    zoom_start=10
)

st_folium(m, width=700, height=500)