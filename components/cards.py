import streamlit as st

def metric_card(title, value, color):

    st.markdown(f"""
<div class="metric-card">

<h4>{title}</h4>

<h1 style="color:{color};">
{value}
</h1>

</div>
""", unsafe_allow_html=True)