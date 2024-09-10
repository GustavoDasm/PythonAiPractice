import numpy as np
import matplotlib.pyplot as plt

image = np.array([
    [250, 0, 0],
    [0, 250, 0],
    [0, 0, 250]
])

plt.imshow(image, cmap='gray', vmin=0, vmax=255)
plt.colorbar()
plt.show()