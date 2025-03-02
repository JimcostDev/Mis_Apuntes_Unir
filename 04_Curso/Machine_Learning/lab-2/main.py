
"""
Modelo sencillo mediante árboles de clasificación en Python

Este laboratorio tiene como objetivo aplicar un algoritmo de clasificación (árbol de decisión)
para predecir la variable respuesta "Chance of Admit" a partir de un conjunto de datos de admisiones
a estudios de posgrado obtenido desde Kaggle. Se transforma la probabilidad en una variable categórica:
se asigna "yes" si la probabilidad es ≥ 0.6 y "no" en caso contrario.

El laboratorio demuestra el uso de técnicas básicas de machine learning para transformar una variable
continua en categórica y entrenar un modelo de árbol de decisión. La evaluación inicial muestra resultados
que pueden mejorarse mediante técnicas adicionales de ajuste de parámetros y validación.
"""
# pip install kagglehub[pandas-datasets]
# pip install scikit-learn matplotlib pandas numpy

# Importar las librerías necesarias
import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt

# ---------------------------
# 1. Carga y Análisis del Dataset
# ---------------------------

# Establecer el path del archivo a cargar
file_path = "Admission_Predict.csv"  

# Cargar la última versión del dataset usando kagglehub
df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "mohansacharya/graduate-admissions",
    file_path,
)

print("Primeras 5 registros del dataset:")
print(df.head())

# Crear la variable respuesta 'admit' según el criterio: ≥ 0.6 -> 'yes', de lo contrario 'no'
df['admit'] = np.where(df['Chance of Admit '] >= 0.6, 'yes', 'no')

# Eliminar la columna original de probabilidad
df = df.drop(columns=['Chance of Admit '])

# Verificar la existencia de valores faltantes
print("\nValores faltantes por columna:")
print(df.isnull().sum())

# Análisis descriptivo de las variables
print("\nEstadísticas descriptivas:")
print(df.describe())

# ---------------------------
# 2. División del Conjunto de Datos
# ---------------------------

# Definir las variables predictoras (X) y la variable respuesta (y)
X = df.drop(columns=['admit'])
y = df['admit']

# Dividir el dataset en conjunto de entrenamiento (70%) y de prueba (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print("\nDimensiones de los conjuntos:")
print("Entrenamiento:", X_train.shape, "Prueba:", X_test.shape)

# ---------------------------
# 3. Construcción y Evaluación del Modelo
# ---------------------------

# Crear y entrenar el modelo de árbol de decisión
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Realizar predicciones sobre el conjunto de prueba
y_pred = clf.predict(X_test)

# Evaluar el desempeño del modelo
accuracy = accuracy_score(y_test, y_pred)
print("\nExactitud del modelo:", accuracy)

print("\nMatriz de confusión:")
print(confusion_matrix(y_test, y_pred))

print("\nReporte de clasificación:")
print(classification_report(y_test, y_pred))

# Visualizar el árbol de decisión
plt.figure(figsize=(18,8))
plot_tree(clf, feature_names=X.columns, class_names=['no', 'yes'], filled=True)
plt.title("Árbol de Decisión")
plt.show()

