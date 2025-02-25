import matplotlib.pyplot as plt
from nltk import FreqDist
from wordcloud import WordCloud

def plot_frequency(tokens, title):
    """
    Genera un gráfico de barras con los 15 términos más frecuentes.
    """
    freq_dist = FreqDist(tokens)
    most_common = freq_dist.most_common(15)
    words, counts = zip(*most_common)
    plt.figure(figsize=(10, 5))
    plt.bar(words, counts, color='skyblue')
    plt.title(f"15 términos más frecuentes en {title}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_wordcloud(tokens, title):
    """
    Genera una nube de palabras a partir de la distribución de frecuencias.
    """
    freq_dist = FreqDist(tokens)
    wordcloud = WordCloud(width=800, height=400, background_color='white') \
                  .generate_from_frequencies(freq_dist)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f"Nube de palabras de {title}")
    plt.show()
