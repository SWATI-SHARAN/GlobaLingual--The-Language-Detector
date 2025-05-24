import streamlit as st
from pathlib import Path
from PIL import Image

# Page setup from second block overrides first layout setting to centered as you requested
st.set_page_config(page_title="GlobaLingual", page_icon="logo1.png", layout="centered")

# ⬇️ ADD CSS block from second snippet here
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #ffc0cb, #ff69b4, #ffb6c1);
            color: white;
        }
        .stButton>button {
            background-color: white;
            color: #d63384;
            border: none;
            padding: 0.6rem 1.2rem;
            font-size: 1.1rem;
            border-radius: 10px;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #d63384;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Background Gradient with CSS from first snippet (note: this will be overridden by .stApp in above CSS)
page_bg = """
<style>
body {
    background: linear-gradient(135deg, #f2f0ff, #d6f0ff);
    font-family: 'Segoe UI', sans-serif;
    margin: 0;
    padding: 0;
}
header, footer, .css-18e3th9, .css-1d391kg {  /* Hide default Streamlit menu, footer, sidebar */
    visibility: hidden;
}
.header-title {
    font-size: 3em;
    font-weight: bold;
    color: #4b4b76;
    margin-bottom: 0;
    text-align: center;
}
.tagline {
    font-size: 1.3em;
    font-style: italic;
    color: #5c5c8a;
    text-align: center;
}
.logo-img {
    width: 200px;
    margin-bottom: 20px;
    display: block;
    margin-left: auto;
    margin-right: auto;
}
.floating-icons {
    font-size: 1.6em;
    margin-top: 10px;
    text-align: center;
}
.center-text {
    text-align: center;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Logo path (safe loading)
logo_path = Path(__file__).parent / "logo1.png"
if not logo_path.exists():
    st.error(f"Logo not found at: {logo_path}")
else:
    st.image(logo_path, use_container_width=True)

# Centered content
st.markdown('<h1 class="header-title">GlobaLingual</h1>', unsafe_allow_html=True)
st.markdown('<p class="tagline">🌍 Universal language detection made simple.</p>', unsafe_allow_html=True)
st.markdown('<div class="floating-icons">🗣️ 📝 🌐 🎧</div>', unsafe_allow_html=True)
st.markdown('<p class="center-text">Detect text, voice, and files across multiple languages with ease.</p>', unsafe_allow_html=True)

# Button to navigate to main app
if st.button("🚀 Start Detecting"):
    st.switch_page("pages/app.py")
