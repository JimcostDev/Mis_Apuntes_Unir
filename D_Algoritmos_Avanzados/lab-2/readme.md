## Puzle de las losetas

Este proyecto resuelve el puzle de las losetas utilizando el algoritmo A*. El puzle de las losetas es un juego en el que se tienen 15 losetas numeradas y un espacio vacío en una cuadrícula de 4x4. El objetivo es reorganizar las losetas desde una configuración inicial hasta una configuración objetivo.

## Descripción del Código

### Clase `Puzzle`

La clase `Puzzle` representa una instancia del puzle de las losetas. Cada instancia contiene un estado del puzle y puede generar sus posibles movimientos.

#### Métodos:

- **`__init__(self, estado, objetivo, pasos=None, costo=0)`**: Inicializa una instancia de la clase `Puzzle`.
  - **Parámetros:**
    - `estado` (list): Lista que representa la configuración actual del puzle.
    - `objetivo` (list): Lista que representa la configuración objetivo del puzle.
    - `pasos` (list, optional): Lista de estados alcanzados hasta el momento. Por defecto es None.
    - `costo` (int, optional): Valor que representa el costo acumulado para llegar al estado actual. Por defecto es 0.

- **`es_objetivo(self)`**: Verifica si el estado actual es igual al estado objetivo.
  - **Retorno:** `True` si el estado actual es el objetivo, `False` de lo contrario.

- **`generar_hijos(self)`**: Genera los estados hijos resultantes de cada acción posible (arriba, abajo, izquierda, derecha).
  - **Retorno:** Lista de instancias de la clase `Puzzle` que representan los estados hijos.

- **`heuristica(self)`**: Calcula la heurística utilizando la distancia de Manhattan.
  - **Retorno:** Valor numérico que representa la heurística del estado actual.

- **`costo_total(self)`**: Calcula el costo total como la suma de la heurística y el costo acumulado.
  - **Retorno:** Valor numérico que representa el costo total del estado actual.

- **`__lt__(self, other)`**: Define la comparación `<` entre instancias de la clase `Puzzle` para ser utilizada en la cola de prioridad.
  - **Parámetros:**
    - `other`: Otra instancia de la clase `Puzzle`.
  - **Retorno:** `True` si el costo total de la instancia actual es menor que el de `other`, `False` de lo contrario.

### Función `es_alcanzable(estado_inicial, estado_objetivo)`

Esta función verifica si la configuración objetivo es alcanzable desde la configuración inicial basándose en la paridad de las inversiones.

- **Parámetros:**
  - `estado_inicial` (list): Lista que representa la configuración inicial del puzle.
  - `estado_objetivo` (list): Lista que representa la configuración objetivo del puzle.
- **Retorno:** `True` si la configuración objetivo es alcanzable, `False` de lo contrario.

### Función `resolver_puzzle(estado_inicial, estado_objetivo)`

Esta función resuelve el puzle de las losetas utilizando el algoritmo A*.

- **Parámetros:**
  - `estado_inicial` (list): Lista que representa la configuración inicial del puzle.
  - `estado_objetivo` (list): Lista que representa la configuración objetivo del puzle.
- **Retorno:** Un mensaje indicando si se encontró o no una solución, junto con los pasos y el tiempo de ejecución.

## Conceptos Técnicos

### Heurística

En el contexto del algoritmo A*, la heurística es una estimación del costo restante para alcanzar la meta desde el estado actual. En este proyecto, se utiliza la **distancia de Manhattan** como heurística. La distancia de Manhattan se calcula como la suma de las distancias horizontales y verticales entre las losetas y su posición objetivo.

### Algoritmo A*

El **algoritmo A*** es un algoritmo de búsqueda y de camino óptimo que utiliza una combinación de **costo acumulado** y **heurística** para encontrar la solución más eficiente. La función `costo_total(self)` en la clase `Puzzle` suma el costo acumulado (número de movimientos realizados) y la heurística para determinar la prioridad de los estados en la cola de prioridad.

### Paridad de Inversiones

La **paridad de inversiones** es una propiedad que determina si una configuración del puzle es alcanzable desde otra. Una inversión es cuando una loseta precede a otra loseta de menor número en la secuencia del puzle (excluyendo el espacio vacío). La paridad de inversiones debe ser la misma tanto en el estado inicial como en el objetivo para que la configuración objetivo sea alcanzable.

## Ejemplo de uso

A continuación se muestra un ejemplo de cómo utilizar el código para resolver el puzle:

```python
if __name__ == "__main__":
    ESTADO_INICIAL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
    ESTADO_OBJETIVO = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    RESULTADO = resolver_puzzle(ESTADO_INICIAL, ESTADO_OBJETIVO)
    print(RESULTADO)
```
