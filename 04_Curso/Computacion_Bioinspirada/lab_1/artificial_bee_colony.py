# Implementación  del algoritmo Artificial Bee Colony (ABC).
import random
import numpy as np
import matplotlib.pyplot as plt

def funcion_esfera(x):
    """Función Sphere: f(x) = sum(x_i^2). Objetivo: minimizar"""
    return sum(xi*xi for xi in x)

def aptitud_desde_objetivo(valor_objetivo):
    """Convierte un valor objetivo (a minimizar) a aptitud (a maximizar)."""
    if valor_objetivo >= 0:
        return 1.0 / (1.0 + valor_objetivo)
    else:
        return 1.0 + abs(valor_objetivo)

def abc_colonia(funcion_objetivo, limites, num_empleadas=20, iter_max=200, limite_scouter=50, semilla=None):
    """
    Implementación del algoritmo Artificial Bee Colony (ABC).
    Devuelve: mejor_solucion, mejor_valor, historial_mejor
    """
    if semilla is not None:
        random.seed(semilla)
        np.random.seed(semilla)
    D = len(limites)
    SN = num_empleadas
    fuentes = [np.array([random.uniform(limites[d][0], limites[d][1]) for d in range(D)]) for _ in range(SN)]
    valores_obj = [funcion_objetivo(f) for f in fuentes]
    aptitudes = [aptitud_desde_objetivo(v) for v in valores_obj]
    intentos = [0] * SN
    historial_mejor = []
    indice_mejor = int(np.argmin(valores_obj))
    mejor_solucion = fuentes[indice_mejor].copy()
    mejor_valor = valores_obj[indice_mejor]
    for it in range(iter_max):
        for i in range(SN):
            k = random.choice([x for x in range(SN) if x != i])
            phi = np.random.uniform(-1, 1, size=D)
            candidato = fuentes[i] + phi * (fuentes[i] - fuentes[k])
            for d in range(D):
                lo, hi = limites[d]
                if candidato[d] < lo:
                    candidato[d] = lo
                if candidato[d] > hi:
                    candidato[d] = hi
            valor_cand = funcion_objetivo(candidato)
            fit_cand = aptitud_desde_objetivo(valor_cand)
            if fit_cand > aptitudes[i]:
                fuentes[i] = candidato
                valores_obj[i] = valor_cand
                aptitudes[i] = fit_cand
                intentos[i] = 0
            else:
                intentos[i] += 1
        suma_apt = sum(aptitudes)
        if suma_apt == 0:
            probabilidades = [1.0/SN] * SN
        else:
            probabilidades = [a/suma_apt for a in aptitudes]
        contador_onlooker = 0
        idx = 0
        while contador_onlooker < SN:
            if random.random() < probabilidades[idx]:
                k = random.choice([x for x in range(SN) if x != idx])
                phi = np.random.uniform(-1, 1, size=D)
                candidato = fuentes[idx] + phi * (fuentes[idx] - fuentes[k])
                for d in range(D):
                    lo, hi = limites[d]
                    if candidato[d] < lo:
                        candidato[d] = lo
                    if candidato[d] > hi:
                        candidato[d] = hi
                valor_cand = funcion_objetivo(candidato)
                fit_cand = aptitud_desde_objetivo(valor_cand)
                if fit_cand > aptitudes[idx]:
                    fuentes[idx] = candidato
                    valores_obj[idx] = valor_cand
                    aptitudes[idx] = fit_cand
                    intentos[idx] = 0
                else:
                    intentos[idx] += 1
                contador_onlooker += 1
            idx = (idx + 1) % SN
        for i in range(SN):
            if intentos[i] > limite_scouter:
                fuentes[i] = np.array([random.uniform(limites[d][0], limites[d][1]) for d in range(D)])
                valores_obj[i] = funcion_objetivo(fuentes[i])
                aptitudes[i] = aptitud_desde_objetivo(valores_obj[i])
                intentos[i] = 0
        indice_actual_mejor = int(np.argmin(valores_obj))
        if valores_obj[indice_actual_mejor] < mejor_valor:
            mejor_valor = valores_obj[indice_actual_mejor]
            mejor_solucion = fuentes[indice_actual_mejor].copy()
        historial_mejor.append(mejor_valor)
        if (it+1) % 50 == 0 or it == 0 or it == iter_max-1:
            print(f"Iteración {it+1}/{iter_max} - Mejor valor actual: {mejor_valor:.6e}")
    return mejor_solucion, mejor_valor, historial_mejor

if __name__ == "__main__":
    D = 10
    limites = [(-5.12, 5.12)] * D
    num_empleadas = 30
    iter_max = 300
    limite_scouter = 60
    semilla = 42
    mejor_sol, mejor_val, historial = abc_colonia(funcion_esfera, limites,
                                                  num_empleadas=num_empleadas,
                                                  iter_max=iter_max,
                                                  limite_scouter=limite_scouter,
                                                  semilla=semilla)
    print("\nRESULTADO FINAL")
    print("Mejor valor (Sphere):", mejor_val)
    print("Mejor solución (primeros 10 componentes):", np.round(mejor_sol, 6).tolist())
    # Gráfica de convergencia
    import matplotlib.pyplot as plt
    plt.figure(figsize=(6,4))
    plt.plot(historial)
    plt.title("Convergencia ABC sobre Sphere (D=10)")
    plt.xlabel("Iteración")
    plt.ylabel("Mejor valor (mínimo encontrado)")
    plt.grid(True)
    plt.show()
