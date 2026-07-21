from scipy.optimize import minimize

def utilidad(v):
    x, y = v
    return -x**2 - y**2 - x*y + 40*x + 50*y - 600

# Minimizamos el negativo de la utilidad
def objetivo(v):
    return -utilidad(v)

limites = [(0, None), (0, None)]
iteracion = [0]



def mostrar_avance(v):
    iteracion[0] += 1
    print(f"Iteración {iteracion[0]}: x={v[0]:.4f}, y={v[1]:.4f}, utilidad={utilidad(v):.4f}")

resultado = minimize(objetivo, x0=[0, 0], method='L-BFGS-B', callback=mostrar_avance,bounds=limites )

x_opt, y_opt = resultado.x
utilidad_opt = -resultado.fun

print(f"\nBotellas chicas óptimas: {x_opt:.2f} (miles/día)")
print(f"Botellas grandes óptimas: {y_opt:.2f} (miles/día)")
print(f"Utilidad máxima: ${utilidad_opt:,.2f}")

