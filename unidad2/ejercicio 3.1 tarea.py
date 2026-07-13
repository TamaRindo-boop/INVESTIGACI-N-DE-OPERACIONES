import numpy as np

# ===========================
# Función de costo
# ===========================
def f(x, y):
    return x**2 + y**2 + x*y + 30000*x + 45000*y + 600000

# ===========================
# Gradiente de la función
# ===========================
def gradiente(x, y):
    dfx = 2*x + y + 30000
    dfy = x + 2*y + 45000
    return np.array([dfx, dfy])

# ===========================
# Callback
# Guarda cada iteración
# ===========================
historial = []

def callback(iteracion, x, y, costo):
    historial.append((iteracion, x, y, costo))

# ===========================
# Parámetros del método
# ===========================
alpha = 0.00001          # Tasa de aprendizaje
tolerancia = 1e-6
max_iter = 100000

# Punto inicial
x = 10.0
y = 10.0

# ===========================
# Descenso por gradiente
# ===========================
for i in range(max_iter):

    # Guardar información
    callback(i, x, y, f(x, y))

    # Calcular gradiente
    grad = gradiente(x, y)

    # Verificar convergencia
    if np.linalg.norm(grad) < tolerancia:
        break

    # Actualizar variables
    x = x - alpha * grad[0]
    y = y - alpha * grad[1]

# ===========================
# Resultados
# ===========================
print("Iteraciones:", i + 1)
print("x =", x)
print("y =", y)
print("Costo mínimo =", f(x, y))

# Mostrar las primeras 10 iteraciones
print("\nPrimeras iteraciones:")
for dato in historial[:10]:
    print(dato)