## Puzle de las losetas

Este proyecto resuelve el puzle de las losetas utilizando el algoritmo A*. El puzle de las losetas es un juego en el que se tienen n losetas numeradas y un espacio vacío en una cuadrícula de nxn. El objetivo es reorganizar las losetas desde una configuración inicial hasta una configuración objetivo.

## Descripción del Código

### Clase `Puzzle`

La clase `Puzzle` representa una instancia del puzle de las losetas. Cada instancia contiene un estado del puzle y puede generar sus posibles movimientos.

#### Métodos:

- **`__init__(self, estado, objetivo, pasos=None, costo=0, tamano=4)`**: Inicializa una instancia de la clase `Puzzle`.
  - **Parámetros:**
    - `estado` (list): Lista que representa la configuración actual del puzle.
    - `objetivo` (list): Lista que representa la configuración objetivo del puzle.
    - `pasos` (list, optional): Lista de estados alcanzados hasta el momento. Por defecto es None.
    - `costo` (int, optional): Valor que representa el costo acumulado para llegar al estado actual. Por defecto es 0.
    - `tamano` (int): Tamaño del lado del puzzle (n x n).

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

### Función `contar_inversiones(lista)`

Esta función cuenta el número de inversiones en una lista de números, excluyendo el 0.

- **Parámetros:**
  - `lista` (list): Lista de números para contar las inversiones.
- **Retorno:**
  - `int`: El número de inversiones.

### Función `es_alcanzable(estado_inicial, estado_objetivo, tamano)`

Esta función verifica si la configuración objetivo es alcanzable desde la configuración inicial basándose en la paridad de las inversiones y la posición del espacio vacío.

- **Parámetros:**
  - `estado_inicial` (list): Lista que representa la configuración inicial del puzle.
  - `estado_objetivo` (list): Lista que representa la configuración objetivo del puzle.
  - `tamano` (int): Tamaño del lado del puzzle (n x n).
- **Retorno:** 
  - `bool`: `True` si la configuración objetivo es alcanzable, `False` de lo contrario.
  - `str`: Razón detallada si la configuración no es alcanzable.

### Función `resolver_puzzle(estado_inicial, estado_objetivo, tamano)`

Esta función resuelve el puzle de las losetas utilizando el algoritmo A*.

- **Parámetros:**
  - `estado_inicial` (list): Lista que representa la configuración inicial del puzle.
  - `estado_objetivo` (list): Lista que representa la configuración objetivo del puzle.
  - `tamano` (int): Tamaño del lado del puzzle (n x n).
- **Retorno:** Un mensaje indicando si se encontró o no una solución, junto con los pasos y el tiempo de ejecución.

### Función `obtener_entrada_usuario()`

Esta función obtiene el tamaño del puzzle y los estados inicial y objetivo del usuario.

- **Retorno:**
  - `tuple`: Tamaño del puzzle, estado inicial y estado objetivo.


---

### Explicación Detallada de las Respuestas

#### Configuración No Alcanzable

Si la configuración objetivo no es alcanzable, se proporciona una explicación detallada de la razón:

- **Paridad de Inversiones (puzzles de tamaño impar):** El número de inversiones en el estado inicial y el estado objetivo deben tener la misma paridad (ambos pares o ambos impares).
- **Suma de Inversiones y Posición del Espacio Vacío (puzzles de tamaño par):** La suma del número de inversiones y la fila del espacio vacío (contando desde 0) debe tener la misma paridad en ambos estados (inicial y objetivo).

#### No se Encontró Solución

Si no se encuentra una solución, aunque el estado objetivo es alcanzable, el mensaje indicará que el algoritmo no logró encontrar la secuencia de movimientos necesaria. Esto puede deberse a limitaciones en el tiempo de ejecución o en la memoria disponibles para explorar todos los posibles estados.

## Conceptos Técnicos

### Heurística

En el contexto del algoritmo A*, la heurística es una estimación del costo restante para alcanzar la meta desde el estado actual. En este proyecto, se utiliza la **distancia de Manhattan** como heurística. La distancia de Manhattan se calcula como la suma de las distancias horizontales y verticales entre las losetas y su posición objetivo.

### Algoritmo A*

El **algoritmo A*** es un algoritmo de búsqueda y de camino óptimo que utiliza una combinación de **costo acumulado** y **heurística** para encontrar la solución más eficiente. La función `costo_total(self)` en la clase `Puzzle` suma el costo acumulado (número de movimientos realizados) y la heurística para determinar la prioridad de los estados en la cola de prioridad.

### Paridad de Inversiones

La **paridad de inversiones** es una propiedad que determina si una configuración del puzle es alcanzable desde otra. Una inversión es cuando una loseta precede a otra loseta de menor número en la secuencia del puzle (excluyendo el espacio vacío). La paridad de inversiones debe ser la misma tanto en el estado inicial como en el objetivo para que la configuración objetivo sea alcanzable.


---
## Explicación de Soluciones en Puzzles de Deslizamiento

### Alcanzabilidad de Estados

Para determinar si un estado objetivo es alcanzable desde un estado inicial en puzzles de deslizamiento, se deben considerar las inversiones y la posición del espacio vacío. Esto es crucial para puzzles 3x3 y 4x4, mientras que para el 2x2, la simplicidad del puzzle reduce la complejidad de este análisis.

#### Puzzles 2x2

En los puzzles 2x2, la resolución es más directa y no siempre requiere un análisis de inversiones debido a la menor cantidad de piezas y movimientos.

- **Ejemplo**:
  - Estado inicial: [1, 0, 2, 3]
  - Estado objetivo: [0, 1, 2, 3]
  - Resultado: Solucionable en 1 paso.

#### Puzzles 3x3 y 4x4

Para estos tamaños, el análisis de inversiones y la posición del espacio vacío son críticos.

- **3x3**:
  - Un puzzle es solucionable si el número de inversiones es par.

- **4x4**:
  - Un puzzle es solucionable si el número de inversiones es par y el espacio vacío está en una fila impar desde abajo, o si el número de inversiones es impar y el espacio vacío está en una fila par desde abajo.

### Resolución con Algoritmo A*

El algoritmo A* es eficaz para puzzles 3x3 y 4x4, garantizando encontrar la solución óptima cuando se usa una heurística adecuada, como la distancia de Manhattan.

- **Distancia de Manhattan**: Suma de las distancias horizontales y verticales de cada pieza desde su posición objetivo.
- **Número de piezas fuera de lugar**: Cuenta las piezas que no están en su posición objetivo.

---

## Ejecución del Programa

Para ejecutar el programa, sigue estos pasos:

1. Asegúrate de tener Python instalado en tu sistema.
2. Guarda el código en un archivo llamado `puzzle.py`.
3. Ejecuta el archivo desde la línea de comandos:

    ```sh
    python puzzle.py
    ```

4. Sigue las instrucciones en la terminal para ingresar el tamaño del puzle, el estado inicial y el estado objetivo.

## Ejemplo de Uso

Supongamos que tienes un puzle de 3x3. Cuando ejecutes el programa, se te pedirá que ingreses el tamaño del puzle, el estado inicial y el estado objetivo. Un ejemplo de entrada y salida es el siguiente:

```sh
Ingrese el tamaño del lado del puzzle (por ejemplo, 3 para un puzzle de 3x3): 3
Ingrese el estado inicial del puzzle (9 números, separados por espacios, con 0 representando el espacio vacío):
1 2 3 4 5 6 7 0 8
Ingrese el estado objetivo del puzzle (9 números, separados por espacios, con 0 representando el espacio vacío):
1 2 3 4 5 6 7 8 0

```
