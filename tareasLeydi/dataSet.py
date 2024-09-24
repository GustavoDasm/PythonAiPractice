import numpy as np
import pandas as pd
from os import system

system('cls')

leerCSV = pd.read_csv('datos/animalDataset.csv')
dfA = pd.DataFrame(leerCSV)

dfA.head()
# Cambiar el nombre de la columna
cambiarNombre = {'Animal': 'Nombre','Height (cm)': 'Alturas(cm)', 'Weight (kg)': 'Peso(kg)'}
dfA.rename(columns=cambiarNombre, inplace=True)

# Mostrar el DataFrames
columnas_a_mostrar = ['Nombre', 'Alturas(cm)']
print(dfA[columnas_a_mostrar].head(10))

