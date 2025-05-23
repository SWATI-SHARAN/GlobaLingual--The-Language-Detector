import streamlit as st
from detector import detect_language_with_confidence, translate_language_name
import speech_recognition as sr
from streamlit_option_menu import option_menu

# Page config
st.set_page_config(page_title="🌍 Language Detector", page_icon="🌐", layout="wide")

# Theme CSS for dark/light mode (overrides Streamlit default)
dark_css = """
<style>
body, .main {
    background-color: #0e1117 !important;
    color: white !important;
}
.stButton>button {
    background-color: #444 !important;
    color: white !important;
}
</style>
"""

light_css = """
<style>
body, .main {
    background-color: white !important;
    color: black !important;
}
.stButton>button {
    background-color: #ddd !important;
    color: black !important;
}
</style>
"""

# Sidebar theme selector (you can also put it top-level)
with st.sidebar:
    st.image("logo.png", width=380)
    theme = st.radio("Select Theme:", ["Light", "Dark"])
    language_display = st.selectbox("Display language names in:", ["English", "Español"])
    lang_map = {"English": "en", "Español": "es"}
    target_lang_code = lang_map[language_display]

if theme == "Dark":
    st.markdown(dark_css, unsafe_allow_html=True)
else:
    st.markdown(light_css, unsafe_allow_html=True)

# Navigation menu with option_menu
selected = option_menu(
    menu_title=None,
    options=["Type Text", "Upload File", "Voice Input"],
    icons=["pencil", "file-earmark-text", "mic-fill"],
    menu_icon="globe",
    default_index=0,
    orientation="horizontal",
)

user_input = ""

if selected == "Type Text":
    st.header("✍️ Type Your Text")
    user_input = st.text_area("Enter text here", height=150)

elif selected == "Upload File":
    st.header("📂 Upload a Text File")
    file = st.file_uploader("Upload .txt file", type=["txt"])
    if file:
        user_input = file.read().decode("utf-8")
        st.text_area("File content preview:", value=user_input, height=150)

elif selected == "Voice Input":
    st.header("🎤 Speak to Detect Language")
    if st.button("🎙️ Start Recording"):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            st.info("Listening...")
            try:
                audio = r.listen(source, timeout=5)
                text = r.recognize_google(audio)
                user_input = text
                st.success(f"You said: {text}")
            except Exception as e:
                st.error("Could not process your voice input.")
    else:
        st.info("Click the button and speak to detect language.")

# Detect button
if st.button("🧠 Detect Language"):
    if user_input.strip() == "":
        st.warning("Please enter, upload, or speak some text.")
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
            st.error("Couldn't detect the language. Try with a longer or clearer text.")
