import streamlit as st
from detector import detect_language_with_confidence, translate_language_name
import speech_recognition as sr
from streamlit_option_menu import option_menu

# Page config
st.set_page_config(page_title="GlobaLingual - Language Detector", page_icon="logo1.png", layout="wide")

# Center logo and heading
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("logo.png", width=500)

# Theme selector at the top (replacing sidebar)
theme = st.radio("🎨 Select Theme", ["Light", "Dark"], horizontal=True)

target_lang_code = st.selectbox(
    "🌐 Select Output Translation Language",
    options=["en", "es", "fr", "de", "hi", "zh", "ar", "ru", "ja", "pt"],
    index=0,
    format_func=lambda code: {
        "en": "English",
        "es": "Spanish",
        "fr": "French",
        "de": "German",
        "hi": "Hindi",
        "zh": "Chinese",
        "ar": "Arabic",
        "ru": "Russian",
        "ja": "Japanese",
        "pt": "Portuguese"
    }.get(code, code)
)

# Theme CSS
dark_css = """
<style>
body, .main, .stApp {
    /* Light pink gradient for dark mode background */
    background: linear-gradient(135deg, #ffe6f0, #ffcce6);
    color: #5a0030 !important;
    font-family: 'Segoe UI', sans-serif;
}
h1, h2, h3, h4, h5, h6, p, label, span, div {
    color: #a33a5a !important;
}
.stButton>button, .stDownloadButton>button {
    background-color: #d966a8 !important;
    color: white !important;
    border-radius: 8px;
}
.stButton>button:hover, .stDownloadButton>button:hover {
    background-color: #c45393 !important;
}
textarea, input, select {
    background-color: #ffe6f0 !important;
    color: #5a0030 !important;
    border: 1px solid #d97aa7 !important;
}
[data-testid="fileUploaderDropzone"] {
    background-color: #ffe6f0 !important;
    border: 2px dashed #d97aa7 !important;
}
</style>
"""

light_css = """
<style>
body, .main, .stApp {
    /* Light pink gradient for light mode background */
    background: linear-gradient(135deg, #fff0f6, #ffd6e8);
    color: #660033 !important;
    font-family: 'Segoe UI', sans-serif;
}
h1, h2, h3, h4, h5, h6, p, label, span, div {
    color: #ec538a !important;
}
.stButton>button, .stDownloadButton>button {
    background-color: #ece0e5 !important;
    color: white !important;
    border-radius: 8px;
}
.stButton>button:hover, .stDownloadButton>button:hover {
    background-color: #cc5c8f !important;
}
textarea, input, select {
    background-color: #fff0f6 !important;
    color: #660033 !important;
    border: 1px solid #e599b2 !important;
}
[data-testid="fileUploaderDropzone"] {
    background-color: #fff0f6 !important;
    border: 2px dashed #e599b2 !important;
}
</style>
"""

st.markdown(dark_css if theme == "Dark" else light_css, unsafe_allow_html=True)

# Session state setup
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# Top menu
selected = option_menu(
    menu_title=None,
    options=["Type Text", "Upload File", "Voice Input"],
    icons=["pencil", "file-earmark-text", "mic-fill"],
    menu_icon="globe",
    default_index=0,
    orientation="horizontal",
)

# Input methods
if selected == "Type Text":
    st.header("✍️ Type Your Text")
    text = st.text_area("Enter text here", height=150)
    if text:
        st.session_state.user_input = text
        st.success("Text saved for detection.")

elif selected == "Upload File":
    st.header("📂 Upload a Text File")
    file = st.file_uploader("Upload .txt file", type=["txt"])
    if file:
        content = file.read().decode("utf-8")
        st.session_state.user_input = content
        st.text_area("File content preview:", value=content, height=150)
        st.success("File text saved for detection.")

elif selected == "Voice Input":
    st.header("🎤 Speak to Detect Language")
    if st.button("🎙️ Start Recording"):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            st.info("Listening...")
            try:
                audio = r.listen(source, timeout=5)
                text = r.recognize_google(audio)
                st.session_state.user_input = text
                st.success(f"You said: {text}")
            except:
                st.error("Could not process your voice input.")

# Language Detection
if st.button("🧠 Detect Language"):
    user_input = st.session_state.user_input.strip()
    if not user_input:
        st.warning("Please enter, upload, or speak some text first.")
    else:
        results = detect_language_with_confidence(user_input)
        if results:
            st.subheader("📊 Detection Results")
            report_lines = []
            for lang_code, lang_name, confidence in results:
                translated_name = translate_language_name(lang_name, target_lang_code)
                output_line = f"{translated_name} ({lang_code}): {confidence}%"
                st.write(f"**{output_line}**")
                report_lines.append(output_line)

            st.download_button(
                label="📥 Download Report",
                data="\n".join(report_lines),
                file_name="language_detection_report.txt",
                mime="text/plain"
            )
        else:
            st.error("Couldn't detect the language. Try with more or clearer text.")
