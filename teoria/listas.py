#LISTAS
lista1 = [1, 2, 3, 4]

#Operaciones y metodos
lista1.append(100) #Añadir elemento nuevo a lista
lista1.insert(0, 200) #Añadir en posicion especifica
lista1.remove(200) #Eliminar elemento por nombre
lista1.pop(0) #Eliminar elemento por index
print("Primera Lista")
for i in lista1:
    print(i , end=' ')

#Slicing
print("\nSegunda Lista")
lista2 = lista1[:2]
for j in lista2:
    print(j , end=' ')

#Unir 2 listas
print("\nTercera Lista lista")
lista3 = lista1 + lista2
for k in lista3:
    print(k , end=' ')

#Ordenar lista
lista4 = lista3.sort(reverse=True) #lista en reversa
print("\nCuarta Lista : Ordenada")
for x in lista3:
    print(x , end=' ')

