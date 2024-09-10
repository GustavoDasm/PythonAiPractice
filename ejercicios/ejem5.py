import numpy as np
from scipy.ndimage import convolve
import matplotlib.pyplot as plt
image = np.array([[1, 2, 3, 0, 0],
                  [4, 5, 6, 0, 0],
                  [7, 8, 9, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0]])

sobel_filter = np.array([[-1, 0, 1],
                         [-2, 0, 2],
                         [-1, 0, 1]])

edge_detected_image = convolve(image, sobel_filter)
plt.figure(figsize=(10, 5))

plt.subplot(1, 2 , 1)
plt.imshow(image, cmap='gray', interpolation='none')
plt.title('Imagen Original')
plt.colorbar()

plt.subplot(1, 2 , 2)
plt.imshow(edge_detected_image, cmap='gray', interpolation='none')
plt.title('Imagen despues de la Convolucion')
plt.colorbar()
plt.show()