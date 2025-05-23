from langdetect import detect_langs
from langdetect.lang_detect_exception import LangDetectException
import pycountry

def detect_language_with_confidence(text):
    try:
        detections = detect_langs(text)
        # Return top 3 candidates with their language code, full name, confidence percentage
        return [(d.lang, get_language_name(d.lang), round(d.prob * 100, 2)) for d in detections[:3]]
    except LangDetectException:
        return []

def get_language_name(lang_code):
    try:
        # pycountry supports ISO 639-1 codes, else return code
        return pycountry.languages.get(alpha_2=lang_code).name
    except:
        return lang_code

def translate_language_name(name, target_lang_code="en"):
    # Simple static translations dictionary fallback
    translations = {
        "English": {"es": "Inglés"},
        "Spanish": {"es": "Español"},
        "French": {"es": "Francés"},
        "German": {"es": "Alemán"},
        # Add more as needed
    }
    if target_lang_code == "en":
        return name
    elif target_lang_code == "es":
        return translations.get(name, {}).get("es", name)
    else:
        return name
