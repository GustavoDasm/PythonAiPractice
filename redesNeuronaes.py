import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import matplotlib.pyplot as plt

# Cargar el conjunto de datos MNIST
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Preprocesar los datos
x_train = x_train.astype('float32') / 255.0  # Normalizar los datos de entrenamiento
x_test = x_test.astype('float32') / 255.0    # Normalizar los datos de prueba
x_train = np.expand_dims(x_train, -1)        # Añadir la dimensión del canal (blanco y negro)
x_test = np.expand_dims(x_test, -1)          # Añadir la dimensión del canal (blanco y negro)

# Crear el modelo
modelo = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),  # Capa convolucional con 32 filtros
    layers.MaxPooling2D((2, 2)),                                            # Capa de max pooling para reducir la resolución
    layers.Conv2D(64, (3, 3), activation='relu'),                           # Capa convolucional con 64 filtros
    layers.MaxPooling2D((2, 2)),                                            # Otra capa de max pooling
    layers.Conv2D(64, (3, 3), activation='relu'),                           # Capa convolucional con 64 filtros
    layers.Flatten(),                                                       # Aplanar las salidas de las capas convolucionales
    layers.Dense(64, activation='relu'),                                    # Capa densa con 64 neuronas
    layers.Dense(10, activation='softmax')                                  # Capa de salida con 10 neuronas (para 10 clases)
])

# Compilar el modelo
modelo.compile(optimizer='adam',                                  # Optimizador Adam
               loss='sparse_categorical_crossentropy',           # Función de pérdida para clasificación múltiple
               metrics=['accuracy'])                             # Métrica de precisión

# Entrenar el modelo
historial = modelo.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

# Evaluar el modelo
pérdida_prueba, precisión_prueba = modelo.evaluate(x_test, y_test, verbose=2)
print(f'\nPrecisión en prueba: {precisión_prueba}')

# Graficar los resultados
plt.plot(historial.history['accuracy'], label='Precisión de entrenamiento')
plt.plot(historial.history['val_accuracy'], label='Precisión de validación')
plt.xlabel('Época')
plt.ylabel('Precisión')
plt.ylim([0, 1])
plt.legend(loc='lower right')
plt.show()
