import streamlit as st


def load_theme():

    st.markdown("""
<style>

.stApp{
background:#061826;
}

.block-container{
padding-top:1rem;
}

h1,h2,h3{
color:white;
}

div[data-testid="stMetric"]{

background:#0D2B45;

padding:15px;

border-radius:12px;

border:1px solid #00CFFF;

box-shadow:0 0 12px rgba(0,255,255,.15);

}

.stButton>button{

width:100%;

height:45px;

border-radius:10px;

background:#00CFFF;

color:white;

font-weight:bold;

border:none;

}

.stButton>button:hover{

background:#00AEEF;

}
.stChatInput{

position:fixed;

bottom:15px;

left:25%;

right:2%;

}
</style>
""", unsafe_allow_html=True)