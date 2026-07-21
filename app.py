import streamlit as st
import datetime

st.set_page_config(
    page_title="KSP IntelliCrime AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================
# Load CSS
# ==========================

with open("styles/app.css") as css:
    st.markdown(
        f"<style>{css.read()}</style>",
        unsafe_allow_html=True
    )

# ==========================
# HEADER
# ==========================

st.markdown("""
<div class="header">

<div class="header-left">
🛡 <span>KSP</span> Crime Intelligence Platform
</div>

<div>

<div class="status">
🟢 ONLINE
</div>

<div class="clock">
""" + datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S") + """
</div>

</div>

</div>
""", unsafe_allow_html=True)

# ==========================
# SIDEBAR
# ==========================

with st.sidebar:

    st.markdown("""
<div class="sidebar-title">
🛡 KSP AI
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="officer-card">
<h3>👮 Officer Profile</h3>
<b>Name</b><br>
Admin Officer
<br><br>
<b>Rank</b><br>
Inspector
<br><br>
<b>ID</b><br>
KSP-001
<br><br>
🟢 Secure Connection

</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
<div class="ai-card">

<h4>🤖 AI STATUS</h4>

✅ Crime Database<br>
✅ Prediction Engine

</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
<div class="online-card">
🟢 SYSTEM ONLINE
</div>
""", unsafe_allow_html=True)

    st.divider()

    st.write("📅", datetime.date.today())
    st.write("⏰", datetime.datetime.now().strftime("%H:%M:%S"))
    st.write("🌐 Karnataka")
    st.write("🛡 Secure Network")
    st.write("🗄 Database : Online")
    st.write("📡 Network : Connected")
    st.write("⚡ CPU Status : Normal")

# ==========================
# Pages
# ==========================

dashboard = st.Page(
    "views/dashboard.py",
    title="Dashboard",
    icon="📊",
    default=True
)



fir = st.Page(
    "views/FIR_upload.py",
    title="FIR Upload",
    icon="📎"
)

report = st.Page(
    "views/export_report.py",
    title="Export Report",
    icon="📄"
)

heatmap = st.Page(
    "views/Crime_heatmap.py",
    title="Crime Heatmap",
    icon="🗺️"
)

network = st.Page(
    "views/network_analysis.py",
    title="Network Analysis",
    icon="👥"
)

prediction = st.Page(
    "views/prediction.py",
    title="Crime Prediction",
    icon="📈"
)

pg = st.navigation(
    [
        dashboard,
        fir,
        report,
        heatmap,
        network,
        prediction
    ],
    position="sidebar"
)

pg.run()