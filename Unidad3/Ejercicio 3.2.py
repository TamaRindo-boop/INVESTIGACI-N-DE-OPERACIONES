from scipy.optimize import minimize

def costo(v):
    x, y = v
    return x**2 + y**2 + x*y + 250*x + 350*y + 5000

iteracion = [0]

def mostrar_avance(v):
    iteracion[0] += 1
    print(f"Iteración {iteracion[0]}: x={v[0]:.4f}, y={v[1]:.4f}, costo={costo(v):.4f}")

resultado = minimize(costo, x0=[0, 0], method='CG', callback=mostrar_avance)
print("\nResultado final:", resultado.x, resultado.fun)

'''
Resolver con el código del gradient CG y BFGS y luego verifiquen con
scipy.optimize.minimize.

¿Cuántos sitios web y cuántos terabytes deberían contratar según el modelo?
¿Qué significa ese "costo mínimo" en pesos al mes?
'''