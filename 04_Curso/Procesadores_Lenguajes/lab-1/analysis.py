from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import matplotlib.pyplot as plt
import nltk
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

def compute_tfidf(documents):
    """
    Calcula la matriz TF-IDF para una lista de documentos.
    """
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    feature_names = vectorizer.get_feature_names_out()
    return tfidf_matrix, feature_names, vectorizer

def get_top_tfidf_terms(tfidf_matrix, feature_names, doc_index, top_n=15):
    """
    Extrae los 'top_n' términos con mayor puntuación TF-IDF para el documento indicado.
    """
    scores = tfidf_matrix[doc_index].toarray()[0]
    top_indices = np.argsort(scores)[-top_n:]
    top_terms = [(feature_names[i], scores[i]) for i in top_indices]
    top_terms = sorted(top_terms, key=lambda x: x[1], reverse=True)
    return top_terms

def plot_top_tfidf_terms(top_terms, title):
    """
    Genera un gráfico de barras para los términos con mayor TF-IDF.
    """
    terms, scores = zip(*top_terms)
    plt.figure(figsize=(10,5))
    plt.bar(terms, scores, color='coral')
    plt.title(f"15 términos con mayor TF-IDF en {title}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def get_top_bigrams(tokens, freq_filter=3, top_n=10):
    """
    Calcula los top_n bigramas (asociaciones) que aparecen al menos 'freq_filter' veces.
    """
    finder = BigramCollocationFinder.from_words(tokens)
    finder.apply_freq_filter(freq_filter)
    bigrams = finder.nbest(BigramAssocMeasures.likelihood_ratio, top_n)
    return bigrams

def get_word_associations(tokens, word, freq_filter=3, top_n=5):
    """
    Busca bigramas que contengan la palabra dada para ver sus asociaciones.
    """
    finder = BigramCollocationFinder.from_words(tokens)
    finder.apply_freq_filter(freq_filter)
    all_bigrams = finder.nbest(BigramAssocMeasures.likelihood_ratio, 50)
    associations = [bigram for bigram in all_bigrams if word in bigram]
    return associations[:top_n]
