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
# LOGIN PAGE
# ==========================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: white;'>🛡️ KSP Crime Intelligence Platform</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #a0aec0;'>Restricted Access. Please log in.</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.info("Sample Credentials — Username: **admin** | Password: **password123**")
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login", use_container_width=True)
            
            if submitted:
                if username == "admin" and password == "password123":
                    st.session_state.logged_in = True
                    st.rerun()
                else:
                    st.error("Invalid username or password")
    
    # Stop execution here if not logged in
    st.stop()

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
    "pages/dashboard.py",
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
    "pages/voice_assistant.py",
    title="Voice Assistant",
    icon="🎤"
)

fir = st.Page(
    "pages/FIR_upload.py",
    title="FIR Upload",
    icon="📎"
)

report = st.Page(
    "pages/export_report.py",
    title="Export Report",
    icon="📄"
)

heatmap = st.Page(
    "pages/Crime_heatmap.py",
    title="Crime Heatmap",
    icon="🗺️"
)

network = st.Page(
    "pages/network_analysis.py",
    title="Network Analysis",
    icon="👥"
)

prediction = st.Page(
    "pages/prediction.py",
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