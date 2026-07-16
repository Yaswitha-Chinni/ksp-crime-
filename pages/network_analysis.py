import streamlit as st
import pandas as pd
import networkx as nx
from pyvis.network import Network
import tempfile
import streamlit.components.v1 as components

st.set_page_config(page_title="Network Analysis", page_icon="👥", layout="wide")

st.title("👥 Criminal Network Analysis")

# ----------------------------
# Load Dataset
# ----------------------------
df = pd.read_csv("data/crime.csv")

df = df.dropna(subset=["Suspect_Name"])

# ----------------------------
# District Filter
# ----------------------------
district = st.selectbox(
    "📍 Select District",
    ["All"] + sorted(df["District"].unique())
)

if district != "All":
    df = df[df["District"] == district]

# =====================================
# ADD SEARCH HERE
# =====================================

suspect = st.text_input("🔍 Search Suspect")

if suspect:
    df = df[
        df["Suspect_Name"].str.contains(
            suspect,
            case=False,
            na=False
        )
    ]

# =====================================
# ADD METRICS HERE
# =====================================

c1, c2, c3 = st.columns(3)

c1.metric("👤 Suspects", df["Suspect_Name"].nunique())
c2.metric("🚔 Crime Types", df["Crime_Type"].nunique())
c3.metric("👮 Stations", df["Police_Station"].nunique())

st.divider()

# =====================================
# CREATE NETWORK GRAPH
# =====================================

G = nx.Graph()

for _, row in df.iterrows():

    suspect = str(row["Suspect_Name"])
    crime = str(row["Crime_Type"])
    station = str(row["Police_Station"])

    G.add_node(suspect, color="red")
    G.add_node(crime, color="orange")
    G.add_node(station, color="blue")

    G.add_edge(suspect, crime)
    G.add_edge(suspect, station)

# =====================================
# DISPLAY GRAPH
# =====================================

net = Network(
    height="700px",
    width="100%",
    bgcolor="#0E1117",
    font_color="white"
)

net.from_nx(G)

tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".html")

net.save_graph(tmp.name)

with open(tmp.name, "r", encoding="utf-8") as f:
    html = f.read()

components.html(html, height=700, scrolling=True)