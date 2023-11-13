# Puzle de las losetas:

## Clase `Puzzle`

### `__init__(self, estado, objetivo, pasos=None, costo=0):`
Inicializa una instancia de la clase `Puzzle`.

- **Parámetros:**
  - `estado`: Lista que representa la configuración actual del puzle.
  - `objetivo`: Lista que representa la configuración objetivo del puzle.
  - `pasos`: Lista opcional de estados alcanzados hasta el momento.
  - `costo`: Valor opcional que representa el costo acumulado para llegar al estado actual.

### `es_objetivo(self):`
Verifica si el estado actual es igual al estado objetivo.

- **Retorno:** Retorna `True` si el estado actual es el objetivo, `False` de lo contrario.

### `generar_hijos(self):`
Genera los estados hijos resultantes de cada acción posible (arriba, abajo, izquierda, derecha).

- **Retorno:** Lista de instancias de la clase `Puzzle` que representan los estados hijos.

### `heuristica(self):`
Calcula la heurística utilizando la distancia de Manhattan.

- **Retorno:** Valor numérico que representa la heurística del estado actual.

### `costo_total(self):`
Calcula el costo total como la suma de la heurística y el costo acumulado.

- **Retorno:** Valor numérico que representa el costo total del estado actual.

### `__lt__(self, other):`
Define la comparación `<` entre instancias de la clase `Puzzle` para ser utilizada en la cola de prioridad.

- **Parámetros:**
  - `other`: Otra instancia de la clase `Puzzle`.
- **Retorno:** Retorna `True` si el costo total de la instancia actual es menor que el de `other`, `False` de lo contrario.

## Función `es_alcanzable(estado_inicial, estado_objetivo)`

### `es_alcanzable(estado_inicial, estado_objetivo):`
Verifica si la configuración objetivo es alcanzable desde la configuración inicial basándose en la paridad.

- **Parámetros:**
  - `estado_inicial`: Lista que representa la configuración inicial del puzle.
  - `estado_objetivo`: Lista que representa la configuración objetivo del puzle.
- **Retorno:** Retorna `True` si la configuración objetivo es alcanzable, `False` de lo contrario.

## Función `resolver_puzzle(estado_inicial, estado_objetivo)`

### `resolver_puzzle(estado_inicial, estado_objetivo):`
Resuelve el puzle de las losetas utilizando el algoritmo A*.

- **Parámetros:**
  - `estado_inicial`: Lista que representa la configuración inicial del puzle.
  - `estado_objetivo`: Lista que representa la configuración objetivo del puzle.
- **Retorno:** Retorna un mensaje indicando si se encontró o no una solución, junto con los pasos y el tiempo de ejecución.

## Ejemplo de uso

```python
estado_inicial = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
estado_objetivo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

resultado = resolver_puzzle(estado_inicial, estado_objetivo)
print(resultado)
