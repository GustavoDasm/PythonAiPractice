def sumar(a, b):
    suma = a + b
    return suma
print(sumar(5,6))

matriz = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]

for fila in matriz:
    # Imprimir cada elemento de la fila separado por espacios
    for elemento in fila:
        print(elemento, end=' ')
    print()