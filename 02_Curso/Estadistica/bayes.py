"""

"""
# Definir las probabilidades iniciales
p_a = 0.3  # Probabilidad de A
p_b_given_a = 0.8  # Probabilidad de B dado A
p_b_given_not_a = 0.4  # Probabilidad de B dado no A

# Calcular la probabilidad de B
p_b = (p_b_given_a * p_a) + (p_b_given_not_a * (1 - p_a))

# Calcular la probabilidad de A dado B usando el teorema de Bayes
p_a_given_b = (p_b_given_a * p_a) / p_b

print("La probabilidad de A dado B es:", p_a_given_b)
