import streamlit as st

def show_alert_bar():
    st.markdown("""
    <style>
    .alert-bar{
        width:100%;
        background:linear-gradient(90deg,#7a0000,#c00000,#7a0000);
        color:white;
        padding:10px;
        border-radius:12px;
        margin-bottom:15px;
        font-weight:bold;
        overflow:hidden;
        white-space:nowrap;
    }

    .alert-text{
        display:inline-block;
        padding-left:100%;
        animation:scroll 18s linear infinite;
    }

    @keyframes scroll{
        0%{transform:translateX(0);}
        100%{transform:translateX(-100%);}
    }
    </style>

    <div class="alert-bar">
        <div class="alert-text">
        🚨 HIGH ALERT • Cyber Fraud Cases Increased • AI Monitoring Active • Secure Network Connected • Karnataka State Police
        </div>
    </div>
    """, unsafe_allow_html=True)