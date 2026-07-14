from scipy.optimize import minimize

def costo(v):
    x, y = v
    return x**2 + y**2 + x*y + 30*x + 45*y + 600

limites = [(0, None), (0, None)]

iteracion = [0]

def mostrar_avance(v):
    iteracion[0] += 1
    print(f"Iteración {iteracion[0]}: x={v[0]:.4f}, y={v[1]:.4f}, costo={costo(v):.4f}")

resultado = minimize(
    costo,
    x0=[10, 10],
    method='L-BFGS-B',
    bounds=limites,
    callback=mostrar_avance
)

print("\nResultado final")
print("x =", resultado.x[0])
print("y =", resultado.x[1])
print("Costo mínimo =", resultado.fun)