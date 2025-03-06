# Importar la librería PuLP
import pulp as pl

# Crear el problema de optimización (tipo "LpProblem")
modelo = pl.LpProblem("Programacion_Peliculas", pl.LpMinimize)

# Ejemplo de función objetivo (minimizar una función arbitraria, pues el objetivo real puede variar)
modelo += 0, "Objetivo"

# Definir diccionarios con las posibles opciones para cada película.
# Cada entrada tendrá la forma: (película, semana_inicio, duracion)
opciones = {
    1: [(1,1), (1,2), (2,1)],
    2: [(1,1), (1,2), (2,1), (2,2), (3,1)],
    3: [(1,1)],  
    4: [(2,1), (2,2), (3,1), (3,2), (4,1)],
    5: [(3,1), (3,2), (3,3), (4,1), (4,2), (4,3), (5,1), (5,2), (6,1)],
    6: [(3,1), (3,2), (3,3), (4,1), (4,2), (5,1)]
}

# Crear variables binarias para cada opción:
x = {}
for i in opciones:
    for (j, k) in opciones[i]:
        var_name = f"x_{i}_{j}_{k}"
        x[(i, j, k)] = pl.LpVariable(var_name, cat="Binary")

# Restricción de selección única por película
for i in opciones:
    modelo += pl.lpSum([x[(i, j, k)] for (j, k) in opciones[i]]) == 1, f"Unico_programa_pelicula_{i}"

# Restricción de capacidad de pantallas por semana
# Se define una función auxiliar que determina si un programa de película i que inicia en j y dura k semanas cubre la semana t
def cubre_semana(j, k, t):
    return (t >= j) and (t < j + k)

# Número de pantallas disponibles
pantallas = 2

# Restricción para cada semana (en este ejemplo consideramos la semana 1 y la semana 3)
semanas_restringidas = [1, 3]

for t in semanas_restringidas:
    # Se suman todas las variables x[(i,j,k)] tales que el programa cubre la semana t
    modelo += pl.lpSum([ x[(i,j,k)] 
                          for i in opciones 
                          for (j,k) in opciones[i] 
                          if cubre_semana(j,k,t) ]) <= pantallas, f"Pantallas_semana_{t}"

# Imprimir el modelo
print(modelo)

