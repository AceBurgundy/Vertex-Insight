from googletrans import Translator # type: ignore

def translate(text: str) -> str:
    """
    Translates a text to english

    Parameters:
    -----------
        - text: (str) = The text to be translated

    Returns:
    --------
        - str: the translated text.
    """
    if text.strip() == '':
        raise TypeError("Text is required to translate")

    translated_object = Translator().translate(text, dest='en')
    return translated_object.text