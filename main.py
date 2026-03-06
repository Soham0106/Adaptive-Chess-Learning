import streamlit as st
from Home_1 import show as show_home
from Puzzles_2 import show as show_puzzles
from chess_app_3 import show as show_chess

# =================== Page config ===================
st.set_page_config(page_title="Adaptive Chess Learning", page_icon="♟", layout="wide")

# =================== CSS Styling ===================
st.markdown("""
<style>
/* Main background and typography */
html, body, .stApp {
    background: linear-gradient(135deg, #9FEDD7 0%, #B8F2E6 100%);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: #026670;
}
.block-container {
    padding: 2rem;
    max-width: 1200px;
    margin: auto;
    background: rgba(237, 234, 229, 0.95);
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}

/* Headings */
h1, h2, h3 {
    color: #026670;
    text-align: center;
    margin-bottom: 1rem;
}
h1 {
    font-size: 2.5rem;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
}

/* Sidebar styling */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #026670 0%, #024950 100%);
}
section[data-testid="stSidebar"] * {
    color: #00BFA5 !important;
}

/* Button styling */
.stButton > button {
    background: linear-gradient(45deg, #FCE181, #FEF9C7);
    color: #026670;
    border-radius: 15px;
    padding: 12px 24px;
    font-weight: bold;
    border: 2px solid transparent;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(252, 225, 129, 0.4);
    width: 100%;
}
.stButton > button:hover {
    background: linear-gradient(45deg, #FEF9C7, #FCE181);
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(252, 225, 129, 0.6);
}
</style>
""", unsafe_allow_html=True)

# =================== Sidebar Navigation ===================
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Puzzles", "Chess App"])

# =================== Show Selected Page ===================
if page == "Home":
    show_home()
elif page == "Puzzles":
    show_puzzles()
elif page == "Chess App":
    show_chess()