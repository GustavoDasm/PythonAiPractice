import pandas as pd;
import numpy as np;
from os import system
system("cls")

def generarCuadrados(n):
    list = [i*i for i in range(1, n + 1)]
    return list

print(generarCuadrados(5))

def generarNombres(num1, num2):
    #Tanto row_names como col_names se generan usando list comprehensions, que son una manera concisa y 
    # eficiente de crear listas en Python.
    list1 = [f"fila {i + 1}" for i in range(num1)] 
    list2 = [f"columna {i + 1}" for i in range(num2)]
    return list1, list2 
#print(generarNombres(3, 4))

def generarDataFrameAleatorio(filas, columnas):  
    data = np.random.rand(filas, columnas) #Crea una matriz de valores randoms
    nombreFilas, nombreColumnas = generarNombres(filas, columnas)
    df = pd.DataFrame(data, index=nombreFilas, columns=nombreColumnas)
    return df

df_1 = generarDataFrameAleatorio(4, 4)
# print(df_1)

# Filtar datos obtener solo las filas donde la col 1 es mayor a 0.5
filtrar = df_1[df_1['columna 1'] > 0.5] 
# print("\nFiltrados (col 1 > 2)\n", filtrar)

def filtrarFilaMayorN(dataF, n):
    suma_filas = dataF.sum(axis=1) #Calcular la suma de cada fila
    filtrado = dataF[suma_filas>n]

    return filtrado
# print(filtrarFilaMayorN(df_1, 2))


# Calcular estadísticas descriptivas
estadisticas = df_1.describe()
# print("\nEstadísticas descriptivas:\n", estadisticas)

# Agrupar datos por columna osea que se repitan y calcular el la media de los numeros random de la columna 2
mediaCol2 = df_1.groupby('columna 1')['columna 2'].mean()
# print("\nMedia de columna 2 por columna 1:\n", mediaCol2)

# Agrupar datos por Ciudad y calcular la media de Edad
# media_edad = df.groupby('Ciudad')['Edad'].mean()
# print("\nMedia de Edad por Ciudad:\n", media_edad)

# Guardar el DataFrame en un archivo CSV
# df.to_csv('datos.csv', index=False)


#--------------------------------------------------
# Crear un Dataframe usando diccionario
pais = ["Peru", "Brasil", "Chile", "Mexico", "Brasil", "Argentina", "Uruguay", "Bolivia", "Estados Unidos"]
poblacion = [10000.555559, 20000.555559, 30000.555559, 40000.555559, 50000.555559, 60000.555559, 70000.555559, 80000.555559, 90000.555559]

diccionario = {'Pais': pais, 'Poblacion':poblacion}
df_2 = pd.DataFrame(diccionario, index=[i for i in range(1, 10)])
system("cls")
print(df_2)

#  leerCSV = pd.read_csv('datos.csv')
# print(leerCSV)

# ---------------------------------------------------
# Metodos

# Mostrar informacion del DataFrame
# print(df_2.info())

# Mostrar n primeras filas
# print(df_2.head(3))

# Mostrar n ultimas filas
# print(df_2.tail(3))

# Mostrar las filas y columnas
# print(df_2.shape)

# ----------------------------------------------------
# Funciones

# Obtener el tamaño del dataframe
print(f"Tamaño del dataframe: {len(df_2)}")

# Obtener el maximo index
print(f"{'Maximo index':>20}: {max(df_2.index)}")

# Obtener el minimo index
print(f"{'Minimo index':>20}: {min(df_2.index)}")

# Obtener el tipo de dato
# print(type(df_2))
# print(type(df_2['Pais'])) ----> Obtener el typo de dato por columna

#Redondear valores del DataFrame
# print(round(df_2, 2))

# Seleccionar una columna con [] 
# print(df_2['Pais'])

# Seleccionar 2 o mas columnas
# print(df_2[['Pais', 'Poblacion']])

# Agregar una nueva columna al dataframe
df_2['Longitud'] = 52


# ---------------------------------------
# NUMPY

# Crear un array de 1000 elementos
array1 = np.arange(0, 9)
print(array1)

# Agregar una nueva columna al dataframe con un array
df_2['Score'] = array1

# Crear numeros enteros del 1 al 100
array2 = np.random.randint(1, 100, size=9)
df_2['Numeros Enteros'] = array2

# Crear numeros decimales del 1 al 100
array3 = np.random.uniform(1, 100, size=9)
df_2['Numeros Decimales'] = array3

# Suma total de una columna
print(f"\nLa suma total es: {df_2['Numeros Enteros'].sum()}")

# Contar, promedio, desv.estandar, maximo y minimo
df_2['Numeros Enteros'].count()
df_2['Numeros Enteros'].mean()
df_2['Numeros Enteros'].std()
df_2['Numeros Enteros'].max()
df_2['Numeros Enteros'].min()
df_2['Numeros Enteros'].describe()   #Describir todo, sum , max... etc

# Calcula suma en una fila
df_2['Promedio E y D'] = (df_2['Numeros Decimales'] + df_2['Numeros Enteros'])/2
print(df_2.round(2))



