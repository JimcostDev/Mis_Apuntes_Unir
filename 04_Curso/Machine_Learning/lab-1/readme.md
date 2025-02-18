# Bike Sharing Data Analysis

Este proyecto realiza un análisis descriptivo del Bike Sharing Dataset (ID=275) de la UCI Machine Learning Repository. Se exploran las características del dataset y se analizan las relaciones entre las variables predictoras y la variable respuesta (*cnt*).

## Objetivos

- Comprender la estructura y distribución del dataset.
- Analizar la relación entre las variables predictoras (por ejemplo, *temp*, *hr*, *season*, etc.) y la variable respuesta (*cnt*).
- Realizar un análisis de correlaciones y visualizar la distribución de las variables.
- Dividir el dataset en conjuntos de entrenamiento (70%) y validación (30%) para futuros procesos de modelización.

## Requisitos

- Python 3.7 o superior
- Dependencias:
  - ucimlrepo
  - pandas
  - matplotlib
  - seaborn
  - scikit-learn

## Instalación

1. **Crear y activar el entorno virtual:**

   - **Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```

2. **Instalar las dependencias:**
   ```bash
   pip install ucimlrepo pandas matplotlib seaborn scikit-learn
   ```