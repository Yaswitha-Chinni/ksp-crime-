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

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown("""
    <div style="text-align: center; margin-top: 50px;">
        <h1 style="color: #00ff88;">🛡️ KSP Security Gateway</h1>
        <p>Please log in to access the Crime Intelligence Platform</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.info("**Sample Credentials:**  \nUsername: `admin`  \nPassword: `password`")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.button("Login", use_container_width=True):
            if username == "admin" and password == "password":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Invalid username or password.")
                
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

    st.markdown('<div id="google_translate_element" style="margin-top:20px; border-radius:10px; overflow:hidden;"></div>', unsafe_allow_html=True)

    import streamlit.components.v1 as components
    components.html("""
    <script>
        const doc = window.parent.document;
        if (!doc.getElementById('google-translate-script')) {
            window.parent.googleTranslateElementInit = function() {
                new window.parent.google.translate.TranslateElement({
                    pageLanguage: 'en',
                    layout: window.parent.google.translate.TranslateElement.InlineLayout.SIMPLE
                }, 'google_translate_element');
            };
            const s = doc.createElement('script');
            s.id = 'google-translate-script';
            s.src = '//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
            doc.head.appendChild(s);
        }
    </script>
    """, height=0, width=0)

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