"""
Autor: Ronaldo Jiménez Acosta
Sitio web: www.jimcostdev.com
Materia: Diseño Avanzado de Algoritmos
Fecha de entrega: 13 de novimbre de 2023
"""
import time
from heapq import heappop, heappush

class Puzzle:
    """Clase que representa el puzle de las losetas."""

    def __init__(self, estado, objetivo, pasos=None, costo=0):
        """
        Inicializa una instancia de la clase Puzzle.

        Parámetros:
        - estado: La configuración actual del puzle.
        - objetivo: La configuración objetivo del puzle.
        - pasos: Lista de estados alcanzados hasta el momento.
        - costo: El costo acumulado para llegar al estado actual.
        """
        self.estado = estado
        self.objetivo = objetivo
        self.pasos = pasos if pasos is not None else [estado]
        self.costo = costo

    def es_objetivo(self):
        """Verifica si el estado actual es el objetivo."""
        return self.estado == self.objetivo

    def generar_hijos(self):
        """
        Genera los estados hijos resultantes de cada acción.

        Retorna:
        - Lista de instancias Puzzle que representan los estados hijos.
        """
        pos_vacio = self.estado.index(0)
        acciones = [
            ('arriba', pos_vacio - 3),
            ('abajo', pos_vacio + 3),
            ('izquierda', pos_vacio - 1),
            ('derecha', pos_vacio + 1)
        ]
        hijos = []
        for accion, nueva_pos in acciones:
            if 0 <= nueva_pos < len(self.estado):
                nuevo_estado = self.estado.copy()
                nuevo_estado[pos_vacio], nuevo_estado[nueva_pos] = nuevo_estado[nueva_pos], nuevo_estado[pos_vacio]
                nuevo_pasos = self.pasos + [nuevo_estado]
                nuevo_costo = self.costo + 1
                hijos.append(Puzzle(nuevo_estado, self.objetivo, nuevo_pasos, nuevo_costo))
        return hijos

    def heuristica(self):
        """Calcula la heurística utilizando la distancia de Manhattan."""
        return sum(abs(i // 4 - self.estado.index(i) // 4) + abs(i % 4 - self.estado.index(i) % 4) for i in range(1, 16))

    def costo_total(self):
        """Calcula el costo total como la suma de la heurística y el costo acumulado."""
        return self.heuristica() + self.costo

    def __lt__(self, other):
        """Define la comparación menor que (<) entre instancias de Puzzle."""
        return self.costo_total() < other.costo_total()

def es_alcanzable(estado_inicial, estado_objetivo):
    """Verifica si la configuración objetivo es alcanzable."""
    def contar_inversiones(lista):
        """Cuenta el número de inversiones en la lista."""
        inversiones = 0
        for i in range(len(lista) - 1):
            for j in range(i + 1, len(lista)):
                if lista[i] > lista[j] and lista[i] != 0 and lista[j] != 0:
                    inversiones += 1
        return inversiones

    return contar_inversiones(estado_inicial) % 2 == contar_inversiones(estado_objetivo) % 2

def resolver_puzzle(estado_inicial, estado_objetivo):
    """
    Resuelve el puzle de las losetas utilizando el algoritmo A*.

    Parámetros:
    - estado_inicial: La configuración inicial del puzle.
    - estado_objetivo: La configuración objetivo del puzle.

    Retorna:
    - Mensaje indicando si se encontró o no una solución.
    """
    if not es_alcanzable(estado_inicial, estado_objetivo):
        return "La configuración objetivo no es alcanzable."

    puzzle_inicial = Puzzle(estado_inicial, estado_objetivo)
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
            return f"¡Siuuuuuuuu! Tiempo de ejecución: {tiempo_ejecucion} segundos"

        estados_visitados.add(tuple(nodo_actual.estado))
        hijos = nodo_actual.generar_hijos()
        hijos_no_visitados = [hijo for hijo in hijos if tuple(hijo.estado) not in estados_visitados]

        for hijo in hijos_no_visitados:
            heappush(nodos_a_explorar, hijo)

    return "No se encontró solución"

# Ejemplo de uso, 0 representa el espacio.
estado_inicial = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
estado_objetivo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

resultado = resolver_puzzle(estado_inicial, estado_objetivo)
print(resultado)