import streamlit as st
import pandas as pd
import plotly.express as px
from components.alert_bar import show_alert_bar
from components.cards import metric_card
show_alert_bar()
st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("🛡 KSP Crime Intelligence Dashboard")

# Load Dataset
df = pd.read_csv("data/crime.csv")

# ==========================
# FILTERS
# ==========================

c1, c2, c3 = st.columns(3)

with c1:
    district = st.selectbox(
        "📍 District",
        ["All"] + sorted(df["District"].unique())
    )

with c2:
    crime = st.selectbox(
        "🚔 Crime Type",
        ["All"] + sorted(df["Crime_Type"].unique())
    )

with c3:
    severity = st.selectbox(
        "⚠ Severity",
        ["All"] + sorted(df["Severity"].unique())
    )

# Apply Filters
if district != "All":
    df = df[df["District"] == district]

if crime != "All":
    df = df[df["Crime_Type"] == crime]

if severity != "All":
    df = df[df["Severity"] == severity]

search = st.text_input(
    "🔍 Search FIR / Victim / Suspect"
)

if search:

    search = search.lower()

    df = df[
        df.astype(str)
        .apply(lambda x: x.str.lower())
        .apply(lambda x: x.str.contains(search))
        .any(axis=1)
    ]

# ==========================
# KPI Cards
# ==========================

c1, c2, c3, c4 = st.columns(4)

with c1:
    metric_card(
        "🚔 Total FIRs",
        len(df),
        "#00ff88"
    )

with c2:
    metric_card(
        "🔴 High Severity",
        len(df[df["Severity"]=="High"]),
        "red"
    )

with c3:
    metric_card(
        "📍 Districts",
        df["District"].nunique(),
        "orange"
    )

with c4:
    metric_card(
        "👮 Police Stations",
        df["Police_Station"].nunique(),
        "cyan"
    )
    
trend = (
    df.groupby("Date")
    .size()
    .reset_index(name="Cases")
)

fig = px.line(
    trend,
    x="Date",
    y="Cases",
    title="📈 Crime Trend"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

top = (
    df["District"]
    .value_counts()
    .head(10)
)

fig = px.bar(
    top,
    title="🏆 Top Crime Districts"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================
# Crime Distribution
# ==========================

crime_chart = px.bar(
    df["Crime_Type"].value_counts(),
    title="Crime Distribution"
)

st.plotly_chart(
    crime_chart,
    use_container_width=True
)

# ==========================
# Two Charts
# ==========================

left, right = st.columns(2)

with left:

    pie = px.pie(
        df,
        names="Crime_Type",
        title="Crime Types"
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )

with right:

    sev = px.pie(
        df,
        names="Severity",
        title="Severity Distribution"
    )

    st.plotly_chart(
        sev,
        use_container_width=True
    )

st.divider()

st.subheader("📋 Recent FIR Records")

st.dataframe(

    df[
        [
            "FIR_No",
            "Crime_Type",
            "District",
            "Police_Station",
            "Severity",
            "Status"
        ]
    ],

    use_container_width=True,

    height=400
)
# ==========================================
# COMMAND CENTER FOOTER
# ==========================================

st.markdown("""
<hr style="border:1px solid #00ff88;">

<div style="
text-align:center;
padding:15px;
color:#8aff8a;
font-family:Consolas;
font-size:15px;
">

🛡 <b>Karnataka State Police Crime Intelligence Platform</b><br><br>

🤖 Powered by Gemini AI &nbsp; | &nbsp;
🗄 Secure Crime Database &nbsp; | &nbsp;
🔒 Secure Network &nbsp; | &nbsp;
📌 Version 2.0

</div>
""", unsafe_allow_html=True)