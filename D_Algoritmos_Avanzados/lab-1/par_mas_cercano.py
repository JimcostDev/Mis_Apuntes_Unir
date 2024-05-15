"""
Autor: Ronaldo Jiménez Acosta
Sitio web: www.jimcostdev.com
Materia: Diseño Avanzado de Algoritmos
Fecha de entrega: 30 de octubre de 2023
"""

import math
import time
import matplotlib.pyplot as plt


def distancia_euclidiana(punto1, punto2):
    """
    Halla la distancia euclidiana entre dos puntos en un plano cartesiano.
    :param punto1: Tupla con las coordenadas (x, y) del primer punto.
    :param punto2: Tupla con las coordenadas (x, y) del segundo punto.
    :return: La distancia euclidiana entre los dos puntos.
    """
    x1, y1 = punto1
    x2, y2 = punto2
    # distancia euclidiana entre dos puntos en un plano cartesiano. 
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) 


def obtener_par_mas_cercano(puntos):
    """
    Halla el par de puntos más cercano en una lista de puntos utilizando el algoritmo de Divide y Vencerás.
    :param puntos: Lista de puntos en un plano cartesiano.
    :return: Una tupla con el par de puntos más cercano y la distancia mínima entre ellos.
    """
    n = len(puntos)

    # caso base de la recursión.
    if n <= 1:
        return None, float('inf')

    if n == 2:
        return puntos, distancia_euclidiana(puntos[0], puntos[1])

    # Ordenar los puntos por su coordenada x
    puntos.sort(key=lambda punto: punto[0])

    # Divide y conquista
    mitad = n // 2
    mitad_izq = puntos[:mitad]
    mitad_der = puntos[mitad:]
    par_izq, distancia_izq = obtener_par_mas_cercano(mitad_izq)
    par_der, distancia_der = obtener_par_mas_cercano(mitad_der)

    # Encuentra la distancia mínima entre los pares de la izquierda y la derecha
    if distancia_izq < distancia_der:
        mejor_par, mejor_distancia = par_izq, distancia_izq
    else:
        mejor_par, mejor_distancia = par_der, distancia_der

    # Comprobar si hay un par más cercano a la línea de división (franja)
    x_mitad = puntos[mitad][0]
    franja = [punto for punto in puntos if abs(punto[0] - x_mitad) < mejor_distancia]
    # Ordenar la lista "franja" por la coordenada y para facilitar la búsqueda.
    franja.sort(key=lambda punto: punto[1])
    for i in range(len(franja)):
        j = i + 1
        # Buscar pares de puntos más cercanos en la franja.
        while j < len(franja) and (franja[j][1] - franja[i][1]) < mejor_distancia:
            # Calcular la distancia entre los puntos i y j de la franja.
            distancia = distancia_euclidiana(franja[i], franja[j])
            # Actualizar si encontramos un par con una distancia menor que "mejor_distancia".
            if distancia < mejor_distancia:
                mejor_distancia = distancia
                mejor_par = [franja[i], franja[j]]
            j += 1
    return mejor_par, mejor_distancia


def leer_archivo(archivo):
    """
    Lee un archivo de texto que contiene las coordenadas de los puntos en un formato específico.
    :param archivo: Nombre del archivo de texto que contiene las coordenadas de los puntos.
    :return: Una lista de tuplas con las coordenadas de los puntos.
    """
    puntos = []
    with open(archivo, 'r') as file:
        lineas = file.read().split('\n')
        for linea in lineas:
            if linea.strip():  # Verifica si la línea no está vacía
                coordenadas = linea.split(',')
                for i in range(0, len(coordenadas), 2):
                    x = int(coordenadas[i])
                    y = int(coordenadas[i + 1])
                    puntos.append((x, y))
    return puntos


def visualizar_puntos(puntos):
    """
    Visualiza los puntos en un gráfico de dispersión.
    :param puntos: Lista de puntos en un plano cartesiano.
    :return: Un gráfico de dispersión que muestra los puntos.
    """
    x, y = zip(*puntos)
    plt.scatter(x, y, label="Puntos")
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.legend()
    plt.show()

def main():
    """
    Función principal del programa que permite al usuario seleccionar un archivo de texto y muestra el par de puntos más cercano.
    """
    while True:
        print("Selecciona el archivo que deseas leer:")
        print("1. datos_100")
        print("2. datos_1000")
        print("3. datos_10000")
        print("4. Salir")

        opcion = input("Ingresa el número de opción: ")

        if opcion == "1":
            archivo = "datos_100.txt"
        elif opcion == "2":
            archivo = "datos_1000.txt"
        elif opcion == "3":
            archivo = "datos_10000.txt"
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")
            continue

        tiempo_inicio = time.time()  # Marca de tiempo de inicio
        puntos = leer_archivo(archivo)
        par_mas_cercano, distancia_minima = obtener_par_mas_cercano(puntos)
        tiempo_fin = time.time()  # Marca de tiempo de finalización

        tiempo_ejecucion = tiempo_fin - tiempo_inicio
        print("El par de puntos más cercano es:", par_mas_cercano)
        print("La distancia mínima es:", round(distancia_minima, 4))
        print("Tiempo de ejecución:", round(tiempo_ejecucion, 4), "segundos")

        # Llama a la función para visualizar los puntos
        visualizar_puntos(puntos)

# entry point
if __name__ == '__main__':
    main()
