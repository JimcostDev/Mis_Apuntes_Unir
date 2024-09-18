import math

# Pedir al usuario que ingrese los coeficientes A, B y C
print('Ingrese los coeficientes A, B y C:')
A = float(input('A: '))
B = float(input('B: '))
C = float(input('C: '))

# Calcular el discriminante
discriminante = B**2 - 4*A*C

# Verificar si la ecuación tiene raíces reales
if discriminante < 0:
    print('La ecuación no tiene raíces reales')
else:
    # Calcular las raíces
    raiz_discriminante = math.sqrt(discriminante)
    X1 = (-B + raiz_discriminante) / (2*A)
    X2 = (-B - raiz_discriminante) / (2*A)
    
    # Mostrar las raíces
    print('X1:', X1)
    print('X2:', X2)
