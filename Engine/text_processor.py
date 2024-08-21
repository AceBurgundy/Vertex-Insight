from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS # type: ignore
from nltk.stem import WordNetLemmatizer # type: ignore
from nltk.tokenize import word_tokenize # type: ignore
from string import punctuation
from pandas import Series # type: ignore
from typing import List

def lower_case(text: str) -> str:
    """
    Converts the input text to lowercase.

    Parameters:
    -----------
        - text (str): Input text.

    Returns:
    --------
        - str: Text converted to lowercase.
    """
    return text.lower()

def remove_punctuation(text: str) -> str:
    """
    Removes punctuation from the input text.

    Parameters:
    -----------
        - text (str): Input text.

    Returns:
    --------
        - str: Text with punctuation removed.
    """
    translation_table = str.maketrans('', '', punctuation)
    return text.translate(translation_table)

def remove_stopwords(text: str) -> str:
    """
    Removes common English stopwords from the input text.

    Parameters:
    -----------
        - text (str): Input text.

    Returns:
    --------
        - str: Text with stopwords removed.
    """
    stop_words = set(ENGLISH_STOP_WORDS)
    return ' '.join([word for word in word_tokenize(text) if word.lower() not in stop_words])

def remove_frequent_words(text: str) -> str:
    """
    Removes frequently occurring words from the input text.

    Parameters:
    -----------
        - text (str): Input text.

    Returns:
    --------
        - str: Text with frequent words removed.
    """
    joined_words = ' '.join(text)
    tokenized_joined_words: List[str] = word_tokenize(joined_words)
    word_count: Series = Series(tokenized_joined_words).value_counts()
    frequent_words: Series = word_count.head(10)
    return ' '.join([word for word in word_tokenize(text) if word not in frequent_words])

def remove_rare_words(text: str) -> str:
    """
    Removes the rare words from the input text.

    Parameters:
    -----------
        - text (str): Input text.

    Returns:
    --------
        - str: Text with the top 10 rare words removed.
    """
    joined_words = ' '.join(text)
    tokenized_joined_words: List[str] = word_tokenize(joined_words)
    word_count: Series = Series(tokenized_joined_words).value_counts()
    rare_words: Series = word_count[word_count == 1].head(10)
    return ' '.join([word for word in word_tokenize(text) if word not in rare_words])

lemmatizer: WordNetLemmatizer = WordNetLemmatizer()

def lemmatize_words(text: str) -> str:
    '''
    Lemmatizes words in the input text.

    Parameters:
    -----------
        - text (str): Input text.

    Returns:
    --------
        - str: Text with lemmatized words.

    Example:
    >>> lemmatized_text = lemmatize_words(input_text)
    >>> print(lemmatized_text)
    Lemmatized version of the input text.
    '''
    return ' '.join([lemmatizer.lemmatize(word) for word in text.split()])

def process_text(text: str) -> str:
    """
    Calls all text processing methods in one go.

    Parameters:
    -----------
        - text (str): Input text.

    Returns:
    --------
        - str: Text after applying all processing methods.
    """
    text = lower_case(text)
    text = remove_punctuation(text)
    text = remove_stopwords(text)
    text = remove_frequent_words(text)
    text = remove_rare_words(text)
    text = lemmatize_words(text)

    return text
