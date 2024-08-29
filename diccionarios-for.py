#DICCIONARIOS
datos = {'Nombre':'Gustavo', 'Edad':15} #Crear diccionario
print(datos['Edad'])
print("\n",datos.keys()) #Ver las keys del diccionario
print("\n",datos.values()) #Ver las values del diccionario
print("\n",datos.items()) #Ver todo del diccionario

#Agregar elemento
datos['Talla'] = 1.5

#Actualizar elemento y agregar otro
datos.update({'Talla': 1.7, 'Lenguajes':['Español', 'Ingles']})
print("\n", datos.items())

#-------------------------------------------------------------------------

#FOR
print("Imprimir listas")
lista = ["perro", "gato", "loro", "cuy"]
for i, listar in enumerate (lista):
    print(f"Lista Numero {i + 1} = {listar}")

#Imprimir diccionarios con for
print("\nImprimir diccionario")
for key, value in datos.items():
    print(f"Key: {key}, Value: {value}")

print("\nFor usando in range")
for i in range(10, 20, 2):
    print(i, end=" ")

    