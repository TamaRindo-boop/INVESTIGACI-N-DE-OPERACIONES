from pulp import LpProblem, LpMinimize, LpVariable, LpStatus, value, LpMaximize

modelo = LpProblem("Aplicacion Movil", LpMinimize)

x = LpVariable("Ilustraciones", lowBound=0)
y = LpVariable("Icon", lowBound=0)

modelo += 40*x + 20*y

modelo += 2*x + y >= 12
modelo += x + y >= 9

modelo.solve()

print("Estado:", LpStatus[modelo.status])
print("Ilustraciones =", value(x))
print("Icon=", value(y))
print("Costo mínimo = $", value(modelo.objective))