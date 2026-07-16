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

✅ Gemini AI<br>
✅ Crime Database<br>
✅ Prediction Engine<br>
✅ Voice Assistant

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
    "pages/Dashboard.py",
    title="Dashboard",
    icon="📊",
    default=True
)

chat = st.Page(
    "pages/AI_chat.py",
    title="AI Crime Assistant",
    icon="🤖"
)

voice = st.Page(
    "pages/Voice_Assistant.py",
    title="Voice Assistant",
    icon="🎤"
)

fir = st.Page(
    "pages/FIR_Upload.py",
    title="FIR Upload",
    icon="📎"
)

report = st.Page(
    "pages/Export_Report.py",
    title="Export Report",
    icon="📄"
)

heatmap = st.Page(
    "pages/Crime_Heatmap.py",
    title="Crime Heatmap",
    icon="🗺️"
)

network = st.Page(
    "pages/Network_Analysis.py",
    title="Network Analysis",
    icon="👥"
)

prediction = st.Page(
    "pages/Prediction.py",
    title="Crime Prediction",
    icon="📈"
)

pg = st.navigation(
    [
        dashboard,
        chat,
        voice,
        fir,
        report,
        heatmap,
        network,
        prediction
    ],
    position="sidebar"
)

pg.run()