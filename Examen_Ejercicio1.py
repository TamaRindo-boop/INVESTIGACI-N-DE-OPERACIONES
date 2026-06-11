from pulp import LpProblem, LpMinimize, LpVariable, LpStatus, value, LpMaximize

modelo = LpProblem("Servicios Web", LpMaximize)

x = LpVariable("Basico", lowBound=0)
y = LpVariable("Avanzado", lowBound=0)

modelo += 30*x + 50*y

modelo += x + 2*y <= 16
modelo += 3*x + 2*y <=24

modelo.solve()

print("Estado:", LpStatus[modelo.status])
print("Basico =", value(x))
print("Avanzado=", value(y))
print("Costo mínimo = $", value(modelo.objective))