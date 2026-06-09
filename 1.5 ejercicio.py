from pulp import *

# Crear modelo de maximización
modelo = LpProblem("Optimizacion_Cluster", LpMaximize)

# Variables de decisión
x = LpVariable("Backend", lowBound=0, cat="Integer")
y = LpVariable("DataWorker", lowBound=0, cat="Integer")

# Función objetivo
modelo += 300 * x + 250 * y, "Rendimiento_Total"

# Restricciones
modelo += 2 * x + y <= 16, "Memoria_RAM"
modelo += x + 2 * y <= 17, "Almacenamiento_SSD"
modelo += x <= 6, "Limite_Backend"
modelo += y <= 7, "Limite_DataWorker"

# Resolver
modelo.solve()

# Resultados
print("Estado:", LpStatus[modelo.status])
print("Backends:", value(x))
print("Data Workers:", value(y))
print("Rendimiento máximo: $", value(modelo.objective), "USD por hora")