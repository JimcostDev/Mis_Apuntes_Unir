import requests
import nltk
import string
from nltk.corpus import stopwords

def download_book(url):
    """
    Descarga el texto desde la URL dada.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error al descargar {url}")
        return ""

def clean_text(text):
    """
    Limpia el texto eliminando encabezados y pies de página típicos de Gutenberg.
    """
    start_marker = "*** START OF THIS PROJECT GUTENBERG EBOOK"
    end_marker = "*** END OF THIS PROJECT GUTENBERG EBOOK"
    start = text.find(start_marker)
    if start != -1:
        text = text[start:]
    end = text.find(end_marker)
    if end != -1:
        text = text[:end]
    return text

def preprocess(text):
    """
    Tokeniza, pasa a minúsculas, elimina tokens no alfabéticos y quita las stopwords.
    """
    tokens = nltk.word_tokenize(text)
    tokens = [word.lower() for word in tokens if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    return tokens
