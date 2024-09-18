# Solicitar al usuario que ingrese los datos separados por comas
datos = input('Ingrese los datos separados por comas: ')

# Convertir los datos en una lista de números
valores = list(map(float, datos.split(',')))

# Encontrar el valor mínimo en la lista de valores
minimo = min(valores)

# Mostrar el valor mínimo
print('El mínimo de los datos ingresados es:', minimo)
