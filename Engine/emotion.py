from textblob import TextBlob

POSITIVE: str = "POSITIVE"
NEGATIVE: str = "NEGATIVE"
NEUTRAL: str = "NEUTRAL"

def get_emotion(text: str):
    """
    Gets the sentiment analyzation of a text

    Parameters:
    -----------
        - text: (str) = The text to be analyzed

    Returns:
    --------
        - (str) = POSITIVE or NEGATIVE or NEUTRAL
    """
    if text.strip() == '':
        raise TypeError("A text is required to get its emotion")

    emotion: float = TextBlob(text).sentiment.polarity
    emotion_label: str = POSITIVE if emotion > 0 else (NEGATIVE if emotion < 0 else NEUTRAL)
    return emotion_label