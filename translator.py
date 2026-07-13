from deep_translator import GoogleTranslator

def translate_text(text, source_lang="auto", target_lang="en"):
    try:
        result = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

def get_supported_languages():
    translator = GoogleTranslator(source="auto", target="en")
    return translator.get_supported_languages(as_dict=True)
