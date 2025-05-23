from langdetect import detect_langs
from langcodes import Language

def detect_language_with_confidence(text):
    try:
        detections = detect_langs(text)
        results = []
        for item in detections:
            lang_code = item.lang
            confidence = round(item.prob * 100, 2)
            lang_name = Language.get(lang_code).display_name()
            results.append((lang_code, lang_name, confidence))
        return results
    except Exception:
        return []

def translate_language_name(name, target_lang_code):
    try:
        return Language.find(name).translate(target_lang_code).display_name()
    except:
        return name
