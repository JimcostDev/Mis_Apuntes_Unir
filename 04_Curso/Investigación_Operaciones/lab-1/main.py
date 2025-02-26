# Importamos la biblioteca PuLP
from pulp import *

# Creamos el problema de maximización
prob = LpProblem("BodyPlus_Optimization", LpMaximize)

# Parámetros de utilidad
profit1 = 371  # Utilidad BodyPlus 100
profit2 = 361  # Utilidad BodyPlus 200

# Definimos las variables de decisión
x1 = LpVariable("x1", lowBound=0)  # BodyPlus 100
x2 = LpVariable("x2", lowBound=0)  # BodyPlus 200

# Añadimos la función objetivo
prob += profit1 * x1 + profit2 * x2, "Total_Profit"

# Añadimos las restricciones
prob += 8 * x1 + 12 * x2 <= 600, "Mecanizado"
prob += 5 * x1 + 10 * x2 <= 450, "Pintura"
prob += 2 * x1 + 2 * x2 <= 140, "Ensamblaje"
prob += x1 - 3 * x2 <= 0, "Mezcla"

# Resolvemos el problema
prob.solve()

# Obtenemos los valores de las variables
x1_value = value(x1)
x2_value = value(x2)

# Mostramos el estado de la solución
print("Estado:", LpStatus[prob.status])

# Mostramos los resultados con redondeo
print("\nResultados:")
print(f"x1 (BodyPlus 100) = {round(x1_value, 2)}")
print(f"x2 (BodyPlus 200) = {round(x2_value, 2)}")
print(f"Utilidad Total = {round(value(prob.objective), 2)}")

# Calculamos manualmente el uso de cada recurso
mechanized_usage = 8 * x1_value + 12 * x2_value
paint_usage = 5 * x1_value + 10 * x2_value
assembly_usage = 2 * x1_value + 2 * x2_value
mix_value = x1_value - 3 * x2_value

# Información sobre las restricciones con cálculo manual
print("\nUso de recursos:")
resources = {
    "Mecanizado": (mechanized_usage, 600),
    "Pintura": (paint_usage, 450),
    "Ensamblaje": (assembly_usage, 140),
    "Mezcla": (mix_value, 0)
}

for name, (usage, limit) in resources.items():
    print(f"{name}: {round(usage, 2)}/{limit} unidades ({round(usage/limit*100 if limit != 0 else 0, 1)}%)")