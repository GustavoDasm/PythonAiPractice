import random
import pyodbc
import pandas as pd

# Datos de conexión
server = 'DESKTOP-GMVV1AK\\SQLEXPRESS'
database = 'TestAi'

try:
    conexion = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    )

    print("Conexion exitosa")

    # Leer datos de la base de datos
    df = pd.read_sql("SELECT * FROM usuarios", conexion)
    print(df)

    cursor = conexion.cursor()

    for i in range(0):
        idProducto = i + 1
        Ventas = random.randint(30, 500)
        query = "INSERT INTO usuarios (idProducto, Ventas) VALUES (?, ?)"
        try:
            cursor.execute(query, (idProducto, Ventas))
            print(f"Registro {i+1} insertado correctamente")
        except Exception as e:
            print(f"Error al insertar registro {i+1}: {e}")

    conexion.commit()

except Exception as e:
    print(f"Error: {e}")

finally:
    # Cerrar la conexión
    if 'conexion' in locals() and conexion is not None:
        conexion.close()
        print("Conexion cerrada")
