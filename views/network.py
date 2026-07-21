import streamlit as st
import pandas as pd

from components.network_graph import build_network



st.title("👥 Criminal Relationship Network")

df = pd.read_csv("data/crime.csv")

graph = build_network(df)

with open(graph, "r", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(
    html,
    height=700,
    scrolling=True
)