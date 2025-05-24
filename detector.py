from langdetect import detect_langs
from deep_translator import GoogleTranslator

def detect_language_with_confidence(text):
    try:
        detected = detect_langs(text)
        return [(d.lang, language_code_to_name(d.lang), round(d.prob * 100, 2)) for d in detected]
    except:
        return []

def language_code_to_name(lang_code):
    mapping = {
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
    }
    return mapping.get(lang_code, lang_code)

def translate_language_name(language_name, target_lang_code="en"):
    if target_lang_code == "en":
        return language_name
    try:
        translated = GoogleTranslator(source='auto', target=target_lang_code).translate(language_name)
        return translated
    except Exception:
        return f"{language_name} (untranslated)"
