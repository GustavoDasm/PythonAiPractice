import tensorflow as tf
import numpy as np

x_train = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
y_train = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

#capa = tf.keras.layers.Dense(units=1, input_shape=[1])
#modelo = tf.keras.Sequential([capa])

oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
oculta2 = tf.keras.layers.Dense(units=3)
salida = tf.keras.layers.Dense(units=1)
modelo = tf.keras.Sequential([oculta1, oculta2, salida])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.01),
    loss='mean_squared_error'
)

print("Comenzando entrenamiento")
historial = modelo.fit(x_train, y_train, epochs=200, verbose=False)
print("Modelo entrenado")

#Matplotlib
import matplotlib.pyplot as plt
plt.xlabel("# Epoca")
plt.ylabel("Magnitud de pérdida")
plt.plot(historial.history["loss"])

print("Hagamos una predicción")
resultado = modelo.predict(np.array([[51.0]]))
print("El resultado es " + str(resultado) + " farenheit!")

#print("Variables internas del modelo")
#print(capa.get_weights())
#print("Variables internas de la capa oculta 1")
#print(oculta1.get_weights())
#print("Variables internas de la capa oculta 2")
#print(oculta2.get_weights())
#print("Variables internas de la capa de salida")
#print(salida.get_weights())