from pulp import *

# Crear modelo de maximización
modelo = LpProblem("Videojuego_Assets", LpMaximize)

# Variables de decisión
x = LpVariable("Personajes", lowBound=0)
y = LpVariable("Escenarios", lowBound=0)

# Función objetivo
modelo += 80*x + 60*y

# Restricciones
modelo += 2*x + y <= 12
modelo += x + 2*y <= 14

# Resolver
modelo.solve()

# Resultados
print("Estado:", LpStatus[modelo.status])
print("Personajes:", value(x))
print("Escenarios:", value(y))
print("Valor máximo: $", value(modelo.objective))