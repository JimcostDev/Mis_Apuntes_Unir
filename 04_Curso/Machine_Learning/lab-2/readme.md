# Modelo sencillo mediante árboles de clasificación en Python

Este laboratorio tiene como objetivo aplicar un algoritmo de clasificación (árbol de decisión)
para predecir la variable respuesta "Chance of Admit" a partir de un conjunto de datos de admisiones
a estudios de posgrado obtenido desde Kaggle. Se transforma la probabilidad en una variable categórica:
se asigna "yes" si la probabilidad es ≥ 0.6 y "no" en caso contrario.

El laboratorio demuestra el uso de técnicas básicas de machine learning para transformar una variable
continua en categórica y entrenar un modelo de árbol de decisión. La evaluación inicial muestra resultados
que pueden mejorarse mediante técnicas adicionales de ajuste de parámetros y validación.

## Descripción

El proyecto sigue los siguientes pasos:

1. **Carga y Preparación de los Datos:**  
   Se utiliza la librería `kagglehub` para cargar el dataset desde Kaggle y `pandas` para manipularlo. La variable "Chance of Admit" se transforma en una variable categórica "admit".

2. **Análisis Descriptivo y División de Datos:**  
   Se realiza un análisis descriptivo, se verifican los valores faltantes y se divide el dataset en conjuntos de entrenamiento y prueba usando `train_test_split`.

3. **Construcción y Evaluación del Modelo:**  
   Se entrena un árbol de decisión con `scikit-learn` y se evalúa su desempeño mediante métricas como exactitud, matriz de confusión y reporte de clasificación. Además, se utiliza `matplotlib` para visualizar el árbol de decisión.

## Instalación

Para instalar las dependencias necesarias, utiliza el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```
También puedes hacer la instalación manual con:

```bash
pip install kagglehub[pandas-datasets]
pip install scikit-learn matplotlib pandas numpy
```