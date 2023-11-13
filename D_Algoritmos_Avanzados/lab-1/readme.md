# Resolución del Problema del Par de Puntos Más Cercano

## Introducción
Este código Python resuelve el problema del par de puntos más cercano utilizando la estrategia de divide y conquista. El objetivo es encontrar el par de puntos en un conjunto dado que tiene la menor distancia euclidiana entre ellos.

## Requisitos
- Python 3.x (se recomienda utilizar la última versión estable de Python).
- Un archivo de texto (.txt) que contenga las coordenadas de los puntos en formato "x y", un punto por línea.

## Funciones Principales

### Función `distancia_euclidiana(punto1, punto2)`
- Esta función calcula la distancia euclidiana entre dos puntos en un plano cartesiano.
- Parámetros:
  - `punto1`: Una tupla que representa el primer punto en formato (x, y).
  - `punto2`: Una tupla que representa el segundo punto en formato (x, y).
- Retorna:
  - La distancia euclidiana entre `punto1` y `punto2`.

### Función `par_mas_cercano_puntos(puntos)`
- Esta función utiliza el algoritmo de divide y conquista para encontrar el par de puntos más cercano en un conjunto de puntos.
- Parámetros:
  - `puntos`: Una lista de tuplas que representan los puntos en formato (x, y).
- Retorna:
  - Una tupla con dos elementos:
    - El par de puntos más cercano encontrado.
    - La distancia euclidiana mínima entre los dos puntos.

## Flujo del Programa

1. Se lee un archivo de texto ("puntos.txt") que contiene las coordenadas de los puntos en un formato específico.
2. Los puntos se almacenan en una lista llamada "puntos".
3. La función `par_mas_cercano_puntos` se llama con la lista de puntos como argumento.
4. La función divide recursivamente la lista de puntos en mitades y encuentra el par de puntos más cercano en cada mitad.
5. Luego, compara la distancia mínima entre los pares de la izquierda y la derecha y el par más cercano en la franja central (una banda alrededor de la línea de división).
6. Devuelve el par de puntos más cercano encontrado y la distancia mínima entre ellos.
7. Se imprime el resultado en la consola.

## Uso

1. Asegúrate de tener un archivo de texto llamado "puntos.txt" con las coordenadas de los puntos en el mismo directorio que el script.
2. Ejecuta el script en un entorno de Python 3.x.

## Ejemplo de Resultado

```markdown
El par de puntos más cercano es: [(x1, y1), (x2, y2)]
La distancia mínima es: distancia
