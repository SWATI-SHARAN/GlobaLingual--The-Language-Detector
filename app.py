import streamlit as st
from detector import detect_language_with_confidence, translate_language_name
import speech_recognition as sr
from streamlit_option_menu import option_menu

# Page config
st.set_page_config(page_title="GlobaLingual- Language Detector", page_icon="logo1.png", layout="wide")

# Centered logo and heading at top of main screen
# Center the logo on the main screen
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("logo.png", width=500)

# Enhanced UI Theme CSS
dark_css = """
<style>
body, .main, .stApp {
    background-color: #0d1117 !important;
    color: #eaeaea !important;
    font-family: 'Segoe UI', sans-serif;
}
[data-testid="stSidebar"] {
    background-color: #161b22 !important;
}
h1, h2, h3, h4, h5, h6, p, label, span, div {
    color: #eaeaea !important;
}
.stButton>button, .stDownloadButton>button {
    background-color: #238636 !important;
    color: white !important;
    border: none;
    border-radius: 8px;
    padding: 0.5rem 1rem;
    font-weight: bold;
    transition: all 0.3s ease-in-out;
}
.stButton>button:hover, .stDownloadButton>button:hover {
    background-color: #2ea043 !important;
}
textarea, input, select {
    background-color: #1c2128 !important;
    color: white !important;
    border: 1px solid #30363d !important;
    border-radius: 6px;
    padding: 0.5rem;
}
[data-testid="fileUploaderDropzone"] {
    background-color: #1c2128 !important;
    border: 2px dashed #444c56 !important;
    border-radius: 6px;
}
</style>
"""

light_css = """
<style>
body, .main, .stApp {
    background-color: #f5f7fa !important;
    color: #1c1c1c !important;
    font-family: 'Segoe UI', sans-serif;
}
[data-testid="stSidebar"] {
    background-color: #ffffff !important;
}
h1, h2, h3, h4, h5, h6, p, label, span, div {
    color: #1c1c1c !important;
}
.stButton>button, .stDownloadButton>button {
    background-color: #0078d4 !important;
    color: white !important;
    border: none;
    border-radius: 8px;
    padding: 0.5rem 1rem;
    font-weight: bold;
    transition: background-color 0.3s ease, transform 0.2s ease;
}
.stButton>button:hover, .stDownloadButton>button:hover {
    background-color: #005ea2 !important;
    transform: scale(1.02);
}
textarea, input, select {
    background-color: #ffffff !important;
    color: #1c1c1c !important;
    border: 1px solid #ccc !important;
    border-radius: 6px;
    padding: 0.5rem;
}
[data-testid="fileUploaderDropzone"] {
    background-color: #ffffff !important;
    border: 2px dashed #ccc !important;
    border-radius: 6px;
}
</style>
"""

# Sidebar
with st.sidebar:
    theme = st.radio("🎨 Select Theme", ["Light", "Dark"])


# Apply CSS
st.markdown(dark_css if theme == "Dark" else light_css, unsafe_allow_html=True)

# Session state for input
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


# Input modes
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

# Detect button
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
