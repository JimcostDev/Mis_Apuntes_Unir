import math

def f(x, A, B, C):
    return A * x**2 + B * x + C

def f_prime(x, A, B):
    return 2 * A * x + B

# Coeficientes de la ecuación cuadrática
print('Ingrese los coeficientes A, B y C:')
A = float(input('A: '))
B = float(input('B: '))
C = float(input('C: '))

# Aproximación inicial
x0 = float(input('Ingrese una aproximación inicial: '))

# Número mínimo de iteraciones
min_iterations = 3

iterations = 0
while iterations < min_iterations:
    # Aplicar el método de Newton-Raphson
    fx = f(x0, A, B, C)
    fpx = f_prime(x0, A, B)
    
    x1 = x0 - fx / fpx
    
    # Actualizar la aproximación
    x0 = x1
    
    iterations += 1

# Mostrar la raíz aproximada
print(f'Una raíz aproximada es: {x0}')
