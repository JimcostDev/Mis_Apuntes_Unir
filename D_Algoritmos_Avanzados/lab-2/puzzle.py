"""
Este módulo resuelve el puzle de las losetas utilizando el algoritmo A*.
El puzle de las losetas es un juego en el que se tienen n losetas numeradas
y un espacio vacío en una cuadrícula de nxn. El objetivo es reorganizar las
losetas desde una configuración inicial hasta una configuración objetivo.
"""
import time
from heapq import heappop, heappush

class Puzzle:
    """Clase que representa el puzle de las losetas."""

    def __init__(self, estado, objetivo, pasos=None, costo=0, tamano=4):
        """
        Inicializa una instancia de la clase Puzzle.

        Parámetros:
        - estado (list): La configuración actual del puzle.
        - objetivo (list): La configuración objetivo del puzle.
        - pasos (list, optional): Lista de estados alcanzados hasta el momento. Default es None.
        - costo (int, optional): El costo acumulado para llegar al estado actual. Default es 0.
        - tamano (int): Tamaño del lado del puzzle (n x n).
        """
        self.estado = estado
        self.objetivo = objetivo
        self.pasos = pasos if pasos is not None else [estado]
        self.costo = costo
        self.tamano = tamano

    def es_objetivo(self):
        """
        Verifica si el estado actual es el objetivo.

        Returns:
        bool: True si el estado actual es el objetivo, False en caso contrario.
        """
        return self.estado == self.objetivo

    def generar_hijos(self):
        """
        Genera los estados hijos resultantes de cada acción.

        Returns:
        list: Lista de instancias Puzzle que representan los estados hijos.
        """
        pos_vacio = self.estado.index(0)
        tamano = self.tamano
        acciones = [
            ('arriba', pos_vacio - tamano),
            ('abajo', pos_vacio + tamano),
            ('izquierda', pos_vacio - 1 if pos_vacio % tamano != 0 else -1),
            ('derecha', pos_vacio + 1 if pos_vacio % tamano != tamano - 1 else -1)
        ]
        hijos = []
        for _, nueva_pos in acciones:
            if 0 <= nueva_pos < len(self.estado) and abs(nueva_pos % tamano - pos_vacio % tamano) <= 1:
                nuevo_estado = self.estado.copy()
                nuevo_estado[pos_vacio], nuevo_estado[nueva_pos] = nuevo_estado[nueva_pos], nuevo_estado[pos_vacio]
                nuevo_pasos = self.pasos + [nuevo_estado]
                nuevo_costo = self.costo + 1
                hijos.append(Puzzle(nuevo_estado, self.objetivo, nuevo_pasos, nuevo_costo, tamano))
        return hijos

    def heuristica(self):
        """
        Calcula la heurística utilizando la distancia de Manhattan.

        Returns:
        int: El valor de la heurística.
        """
        tamano = self.tamano
        return sum(
            abs(i // tamano - self.estado.index(i) // tamano) +
            abs(i % tamano - self.estado.index(i) % tamano)
            for i in range(1, tamano * tamano)
        )

    def costo_total(self):
        """
        Calcula el costo total como la suma de la heurística y el costo acumulado.

        Returns:
        int: El costo total.
        """
        return self.heuristica() + self.costo

    def __lt__(self, other):
        """
        Define la comparación menor que (<) entre instancias de Puzzle.

        Parámetros:
        - other (Puzzle): Otra instancia de Puzzle para comparar.

        Returns:
        bool: True si el costo total de self es menor que el de other, False en caso contrario.
        """
        return self.costo_total() < other.costo_total()


def contar_inversiones(lista):
    """
    Cuenta el número de inversiones en la lista.

    Parámetros:
    - lista (list): Lista de números para contar las inversiones.

    Returns:
    int: El número de inversiones.
    """
    inversiones = 0
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j] and lista[i] != 0 and lista[j] != 0:
                inversiones += 1
    return inversiones

def es_alcanzable(estado_inicial, estado_objetivo, tamano):
    """
    Verifica si la configuración objetivo es alcanzable.

    Parámetros:
    - estado_inicial (list): La configuración inicial del puzle.
    - estado_objetivo (list): La configuración objetivo del puzle.
    - tamano (int): Tamaño del lado del puzzle (n x n).

    Returns:
    bool: True si la configuración objetivo es alcanzable, False en caso contrario.
    str: Razón detallada si la configuración no es alcanzable.
    """
    inversions_inicial = contar_inversiones(estado_inicial)
    inversions_objetivo = contar_inversiones(estado_objetivo)
    pos_vacio_inicial = estado_inicial.index(0) // tamano
    pos_vacio_objetivo = estado_objetivo.index(0) // tamano

    if tamano % 2 == 1:
        alcanzable = inversions_inicial % 2 == inversions_objetivo % 2
    else:
        alcanzable = (inversions_inicial + pos_vacio_inicial) % 2 == (inversions_objetivo + pos_vacio_objetivo) % 2

    if alcanzable:
        razon = "Ambos tienen la misma paridad en la suma de inversiones y posición del espacio vacío."
    else:
        if tamano % 2 == 1:
            razon = "Ambos tienen distinta paridad en la suma de inversiones."
        else:
            razon = "La suma de inversiones y la posición del espacio vacío tienen distinta paridad."
    return alcanzable, razon


def resolver_puzzle(estado_inicial, estado_objetivo, tamano):
    """
    Resuelve el puzle de las losetas utilizando el algoritmo A*.

    Parámetros:
    - estado_inicial (list): La configuración inicial del puzle.
    - estado_objetivo (list): La configuración objetivo del puzle.
    - tamano (int): Tamaño del lado del puzzle (n x n).

    Returns:
    str: Mensaje indicando si se encontró o no una solución.
    """
    alcanzable, razon = es_alcanzable(estado_inicial, estado_objetivo, tamano)
    if not alcanzable:
        return f"La configuración objetivo no es alcanzable. Razón: {razon}"

    puzzle_inicial = Puzzle(estado_inicial, estado_objetivo, tamano=tamano)
    estados_visitados = set()
    nodos_a_explorar = [puzzle_inicial]
    tiempo_inicio = time.time()

    while nodos_a_explorar:
        nodo_actual = heappop(nodos_a_explorar)
        if nodo_actual.es_objetivo():
            tiempo_fin = time.time()
            tiempo_ejecucion = tiempo_fin - tiempo_inicio
            for paso, disposicion in enumerate(nodo_actual.pasos):
                print(f"Paso {paso + 1}: {disposicion}")
            return f"Tiempo de ejecución: {tiempo_ejecucion} segundos"

        estados_visitados.add(tuple(nodo_actual.estado))
        hijos = nodo_actual.generar_hijos()
        hijos_no_visitados = [hijo for hijo in hijos if tuple(hijo.estado) not in estados_visitados]

        for hijo in hijos_no_visitados:
            heappush(nodos_a_explorar, hijo)

    return "No se encontró solución"


def obtener_entrada_usuario():
    """
    Obtiene el tamaño del puzzle y los estados inicial y objetivo del usuario.

    Returns:
    tuple: Tamaño del puzzle, estado inicial y estado objetivo.
    """
    tamano = int(input("Ingrese el tamaño del lado del puzzle (por ejemplo, 3 para un puzzle de 3x3): "))
    print(f"Ingrese el estado inicial del puzzle ({tamano * tamano} números, separados por espacios, con 0 representando el espacio vacío):")
    estado_inicial = list(map(int, input().split()))
    print(f"Ingrese el estado objetivo del puzzle ({tamano * tamano} números, separados por espacios, con 0 representando el espacio vacío):")
    estado_objetivo = list(map(int, input().split()))
    return tamano, estado_inicial, estado_objetivo


if __name__ == "__main__":
    TAMANO, ESTADO_INICIAL, ESTADO_OBJETIVO = obtener_entrada_usuario()
    RESULTADO = resolver_puzzle(ESTADO_INICIAL, ESTADO_OBJETIVO, TAMANO)
    print(RESULTADO)
