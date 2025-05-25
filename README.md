<p align="center">
  <img src="logo.png" alt="Main Logo" width="320"/>
</p>

<h1>
  <img src="logo1.png" alt="Logo" width="90" height="90" align="center">
  GlobaLingual - The Language Detector
</h1>



<p align="center">
  <b>A Streamlit Web App to Instantly Detects Text in Multiple Languages</b>  
</p>

---

##  About the Website

This is an intelligent, interactive web application that lets users **detect** the language of any input text and presents the name of the language with a **confidence value** in another language of their choice. It offers a clean, responsive user interface powered by **Streamlit** and works directly in the browser without any API keys or logins.

---

## Features

-  **Language Detection** using `langdetect`
-  **Translation** between languages using `googletrans`
-  **Real-time UI** powered by Streamlit
-  **Lightweight & Easy to Use**
-  **Minimalistic UI** with dropdowns for easy language selection
-  **Bi-directional translation support**
-  **Deployable on Render/Streamlit Cloud for free**

---

## Tech Stack

### Frontend
- **Streamlit** – for building the web UI
- **HTML/CSS (via Streamlit components)** – for layout and styling

### Backend
- **Python 3.9+**

### Python Libraries Used

| Package          | Purpose                                 |
|------------------|-----------------------------------------|
| `streamlit`      | Web UI framework                        |
| `googletrans==4.0.0rc1` | Translation engine (unofficial Google Translate API) |
| `langdetect`     | Language detection                      |
| `langcodes`      | Language code handling and normalization|
| `speechrecognition` | Speech to text conversion from mic   |
| `pyaudio`        | Audio stream handling for microphone input |
| `pillow`         | Image processing                       |
| `deep-translator`| Additional translation providers       |
| `streamlit-option-menu` | UI navigation menus in Streamlit   |

---

## Additional Information

- The core language detection logic is implemented using a **Naive Bayes classifier** (via the `langdetect` library), which probabilistically determines the most likely language of the input text.
- `pyaudio` is required for microphone audio input and may require additional system dependencies (e.g., `portaudio`).
- The app uses both `googletrans` and `deep-translator` for robust multi-language translation support.

---
## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/GlobaLingual.git
cd GlobaLingual
## 🚀 Getting Started
```
### 2. Install Dependencies

```bash
pip install -r requirements.txt
```
### 3. Run the App

```bash
streamlit run app.py
```
### 4. 🔊 Voice Input (Important)
To use the Voice Input feature, you must install PyAudio.**It is not included by default in many environments it is also not included in the webiste hosted here.
However you can use that feature by installing PyAudio on your system andd running it for using that fearture.**

✅ PyAudio Installation Instructions
For Windows:

If direct installation fails, download the wheel file from:
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

Download the .whl matching your Python version (e.g., PyAudio‑0.2.11‑cp311‑cp311‑win_amd64.whl), then run:
```bash
pip install path_to_downloaded_whl_file.whl
```
