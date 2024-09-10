import numpy as np
pesos = np.array([
    [0.2, 0.8],
    [0.5, 0.1]
])

entradas = np.array([0.6, 0.9])

salidas = np.dot(pesos, entradas)
print("salida de la capa:", salidas)