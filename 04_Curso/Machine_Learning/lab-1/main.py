# Importar librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from ucimlrepo import fetch_ucirepo  # dataset UCI

# Configuración inicial de estilos
# Puedes listar los estilos disponibles con: print(plt.style.available)
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_context('talk')

# 1. Importar el dataset usando ucimlrepo (Bike Sharing Dataset: id=275)
bike_sharing = fetch_ucirepo(id=275)

# Acceso a los datos:
# - Variables predictoras:
X = bike_sharing.data.features
# - Variable respuesta:
y = bike_sharing.data.targets

# Imprimir información de metadatos y variables
print("Metadata del dataset:")
print(bike_sharing.metadata)
print("\nInformación de variables:")
print(bike_sharing.variables)

# 2. Exploración inicial de los datos
# Combinar features y target en un único DataFrame para análisis
df = pd.concat([X, y], axis=1)

print("\nPrimeras filas del DataFrame:")
print(df.head())
print("\nResumen general de la información:")
print(df.info())
print("\nEstadísticas descriptivas:")
print(df.describe())

# 3. División en conjunto de modelización y validación (70% entrenamiento, 30% validación)
train_df, test_df = train_test_split(df, test_size=0.3, random_state=42)
print("\nTamaño del conjunto de entrenamiento:", train_df.shape)
print("Tamaño del conjunto de validación:", test_df.shape)

# 4. Tratamiento de missing values (si existieran)
print("\nValores nulos por columna:")
print(df.isnull().sum())
# En este dataset no se esperan missing values, pero se incluye este paso.
# Si hubiera, se podría usar, por ejemplo:
# df = df.fillna(df.mean())   # Para variables numéricas

# 5. Análisis de correlaciones
# Excluir la columna 'dteday' ya que es de tipo fecha y no se puede convertir a float.
numeric_df = df.drop(columns=['dteday'])
corr_matrix = numeric_df.corr()
print("\nCorrelación de 'cnt' con las demás variables:")
print(corr_matrix['cnt'].sort_values(ascending=False))

# Visualización de la matriz de correlación
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Matriz de Correlación')
plt.tight_layout()
plt.show()

# 6. Análisis de distribuciones y gráficos
# Distribución de la variable respuesta 'cnt'
plt.figure(figsize=(8, 5))
sns.histplot(df['cnt'], kde=True, bins=30)
plt.title('Distribución de la variable respuesta (cnt)')
plt.xlabel('cnt')
plt.ylabel('Frecuencia')
plt.tight_layout()
plt.show()

# Relación entre temperatura y cnt (variable 'temp')
plt.figure(figsize=(8, 5))
sns.scatterplot(x='temp', y='cnt', data=df)
plt.title('Relación entre Temperatura y cnt')
plt.xlabel('Temperatura (normalizada)')
plt.ylabel('cnt')
plt.tight_layout()
plt.show()

# Distribución de cnt por estación ('season')
plt.figure(figsize=(8, 5))
sns.boxplot(x='season', y='cnt', data=df)
plt.title('Distribución de cnt por Estación del Año')
plt.xlabel('Estación (1:invierno, 2:primavera, 3:verano, 4:otoño)')
plt.ylabel('cnt')
plt.tight_layout()
plt.show()
