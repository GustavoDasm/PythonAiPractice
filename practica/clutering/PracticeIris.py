import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Cargar el dataset Iris
iris = load_iris()
X = iris.data
y = iris.target

# Elegir el número de clústeres
num_clusters = 3  # Iris tiene 3 clases

# Crear el modelo KMeans
kmeans = KMeans(n_clusters=num_clusters, random_state=42)

# Ajustar el modelo
kmeans.fit(X)

# Predecir los clústeres
labels = kmeans.labels_

# Reducir la dimensionalidad a 2D
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

# Crear un DataFrame para visualizar los resultados
df = pd.DataFrame(X_reduced, columns=['PCA1', 'PCA2'])
df['Cluster'] = labels
df['Actual'] = y

# Graficar los clústeres
plt.figure(figsize=(10, 6))
plt.scatter(df['PCA1'], df['PCA2'], c=df['Cluster'], cmap='viridis', label='Clúster Predicho', alpha=0.5)
plt.scatter(df['PCA1'], df['PCA2'], c=df['Actual'], cmap='coolwarm', marker='x', label='Clase Real')
plt.title('Clustering del dataset Iris con KMeans')
plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.legend()
plt.show()
