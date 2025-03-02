# Mineria de Texto y PLN

### Integrantes: Ronaldo Jímenez y Bárbara Gómez

Este proyecto implementa tecnicas de mineria de texto y procesamiento de lenguaje natural (PLN) aplicadas a cuatro libros del Proyecto Gutenberg: **Moby Dick**, **Orgullo y Prejuicio**, **Sherlock Holmes** y **Historia de dos ciudades**. El laboratorio extrae los 15 terminos mas frecuentes, genera nubes de palabras, calcula el indice TF-IDF y obtiene asociaciones (bigramas) para analizar la relevancia y el contexto de los terminos en cada obra.

## Dependencias

El proyecto esta desarrollado en Python y utiliza las siguientes librerias:

- `requests`
- `nltk`
- `matplotlib`
- `wordcloud`
- `scikit-learn`
- `pandas` (opcional)

Para instalar las dependencias, puedes ejecutar:

```bash
pip install requests nltk matplotlib wordcloud scikit-learn pandas
```

Adicionalmente, se deben descargar los siguientes recursos de NLTK:
- `punkt`
- `punkt_tab`
- `stopwords`

Estos recursos se pueden descargar automaticamente al ejecutar el script o manualmente utilizando:

```python
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
```

## Estructura del Proyecto

El proyecto se organiza en los siguientes archivos:

```
lab-1/
├── analysis.py        # Funciones para calculo TF-IDF y analisis de bigramas
├── main.py            # Script principal que coordina la ejecucion del laboratorio
├── text_utils.py      # Funciones para descargar, limpiar y preprocesar los textos
└── visualization.py   # Funciones para generar graficos y nubes de palabras
```

## Ejecucion

1. **Crear y activar el entorno virtual:**

   ```bash
   python -m venv env
   # En Windows:
   env\Scripts\activate
   # En macOS/Linux:
   source env/bin/activate
   ```

2. **Instalar las dependencias:**

   ```bash
   pip install requests nltk matplotlib wordcloud scikit-learn pandas
   ```

3. **Ejecutar el script principal:**

   ```bash
   python main.py
   ```

## Descripcion del Proyecto

El laboratorio se desarrollo siguiendo estos pasos:

1. **Descarga y Preprocesamiento del Corpus:**
   - Se descargaron los textos de los libros desde el Proyecto Gutenberg.
   - Se limpio el texto eliminando encabezados y pies de pagina tipicos.
   - Se tokenizo, normalizo a minusculas y eliminaron las stopwords.

2. **Analisis de Frecuencia y Visualizacion:**
   - Se calculo la frecuencia de los terminos y se extrajeron los 15 terminos mas frecuentes para cada libro.
   - Se generaron graficos de barras y nubes de palabras para visualizar estos resultados.

3. **Calculo del Indice TF-IDF:**
   - Se transformaron los libros en documentos y se calculo la matriz TF-IDF.
   - Se extrajeron y visualizaron los 15 terminos con mayor TF-IDF para cada libro.

4. **Analisis de Asociaciones:**
   - Se identificaron bigramas (asociaciones) relevantes en dos de los libros.
   - Se analizaron asociaciones especificas para los terminos **'whale'** en *Moby Dick* y **'elizabeth'** en *Orgullo y Prejuicio*.

## Conclusiones

El laboratorio demuestra como la combinacion de analisis de frecuencia y TF-IDF puede revelar diferentes aspectos del contenido textual. Mientras que la frecuencia resalta las palabras mas comunes, el TF-IDF identifica terminos mas representativos de cada documento. Ademas, el analisis de bigramas permite explorar las asociaciones contextuales entre palabras, ofreciendo una vision mas profunda de la estructura del texto.

