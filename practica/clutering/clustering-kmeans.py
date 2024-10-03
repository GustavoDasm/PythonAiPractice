import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from os import system
system("cls")

df = pd.read_csv('datos/tested.csv')
df.dropna(inplace=True)
df.describe()
print(df.describe())

num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters, random_state=42)

labels = kmeans.labels_

pca = PCA(n_components=2)

df = pd.DataFrame(columns=['PCA1', 'PCA2'])
df['Cluster'] = labels

# Graficar los clústeres
plt.figure(figsize=(10, 6))
plt.scatter(df['PCA1'], df['PCA2'], c=df['Cluster'], cmap='viridis', label='Clúster Predicho', alpha=0.5)
plt.scatter(df['PCA1'], df['PCA2'], c=df['Actual'], cmap='coolwarm', marker='x', label='Clase Real')
plt.title('Clustering del dataset Iris con KMeans')
plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.legend()
plt.show()