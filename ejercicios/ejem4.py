import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
documentos= ["el gato come pescado", "el perro ladra", "el gato juega"]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documentos)

print("Matriz TF-IDF:\n", X.toarray())
print("Vocabulario: ", vectorizer.get_feature_names_out())
