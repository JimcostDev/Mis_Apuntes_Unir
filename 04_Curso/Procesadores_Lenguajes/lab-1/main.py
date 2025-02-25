import nltk
nltk.download('punkt')
nltk.download('punkt_tab') 
nltk.download('stopwords')

from nltk import FreqDist
from text_utils import download_book, clean_text, preprocess
from visualization import plot_frequency, plot_wordcloud
from analysis import compute_tfidf, get_top_tfidf_terms, plot_top_tfidf_terms, get_top_bigrams, get_word_associations

# Definir los libros y sus URLs
books = {
    "Moby Dick": "http://www.gutenberg.org/files/2701/2701-0.txt",
    "Orgullo y Prejuicio": "http://www.gutenberg.org/files/1342/1342-0.txt",
    "Sherlock Holmes": "http://www.gutenberg.org/files/1661/1661-0.txt",
    "Historia de dos ciudades": "http://www.gutenberg.org/files/98/98-0.txt"
}

corpus = {}
processed_corpus = {}

# Descargar, limpiar y procesar cada libro
for title, url in books.items():
    print(f"Descargando {title}...")
    raw_text = download_book(url)
    clean_txt = clean_text(raw_text)
    corpus[title] = clean_txt
    processed_corpus[title] = preprocess(clean_txt)

# Análisis de frecuencia y visualización de cada libro
for title, tokens in processed_corpus.items():
    print(f"\nVisualizando análisis de frecuencia para: {title}")
    plot_frequency(tokens, title)
    plot_wordcloud(tokens, title)

# Preparar documentos (unir tokens) para calcular TF-IDF
documents = []
titles = []
for title, tokens in processed_corpus.items():
    documents.append(" ".join(tokens))
    titles.append(title)

# Calcular TF-IDF para el conjunto de documentos
tfidf_matrix, feature_names, vectorizer = compute_tfidf(documents)

# Mostrar y graficar los 15 términos con mayor TF-IDF para cada libro
for idx, title in enumerate(titles):
    top_tfidf = get_top_tfidf_terms(tfidf_matrix, feature_names, idx, top_n=15)
    print(f"\n{title} - 15 términos con mayor TF-IDF:")
    for term, score in top_tfidf:
        print(f"{term}: {score:.4f}")
    plot_top_tfidf_terms(top_tfidf, title)

# Comparación entre términos más frecuentes y términos con mayor TF-IDF
for title, tokens in processed_corpus.items():
    freq_dist = FreqDist(tokens)
    common_terms = [word for word, _ in freq_dist.most_common(15)]
    print(f"\n{title} - Términos más frecuentes:")
    print(common_terms)

for idx, title in enumerate(titles):
    top_tfidf_terms = [term for term, score in get_top_tfidf_terms(tfidf_matrix, feature_names, idx, top_n=15)]
    print(f"\n{title} - Términos más característicos (TF-IDF):")
    print(top_tfidf_terms)

# Obtención de asociaciones entre palabras
# Ejemplo: Mostrar bigramas (asociaciones) en "Moby Dick" y "Orgullo y Prejuicio"
selected_books = ["Moby Dick", "Orgullo y Prejuicio"]
for book in selected_books:
    tokens = processed_corpus[book]
    bigrams = get_top_bigrams(tokens, freq_filter=3, top_n=10)
    print(f"\n{book} - Top 10 bigramas (asociaciones):")
    for b in bigrams:
        print(b)

# Asociaciones específicas para términos característicos:
associations_moby = get_word_associations(processed_corpus["Moby Dick"], 'whale', freq_filter=3, top_n=5)
associations_pride = get_word_associations(processed_corpus["Orgullo y Prejuicio"], 'elizabeth', freq_filter=3, top_n=5)

print("\nAsociaciones para 'whale' en Moby Dick:")
print(associations_moby)

print("\nAsociaciones para 'elizabeth' en Orgullo y Prejuicio:")
print(associations_pride)
