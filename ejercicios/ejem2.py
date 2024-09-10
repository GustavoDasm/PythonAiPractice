def costo(w):
    return (w - 3) ** 2

def gradiente(w):
    return 2 * (w - 3)

w = 0.0

for i in range(10):
    w = w - 0.1 * gradiente(w)
    print(f"Iteracion {i+1}: w = {w}, costo = {costo(w)}")