import matplotlib.pyplot as plt
from skimage import data, feature
from skimage.filters import (threshold_otsu, threshold_niblack, threshold_sauvola)
from skimage.color import rgb2gray

original = data.astronaut()
grayscale = rgb2gray(original)
edge = feature.canny(grayscale)
fig, axes = plt.subplots(1, 3, figsize=(8, 4))
ax = axes.ravel()

ax[0].imshow(original)
ax[0].set_title("Original")
ax[1].imshow(grayscale, cmap=plt.cm.gray)
ax[1].set_title("Grayscale")
ax[2].imshow(edge, cmap=plt.cm.gray)
ax[2].set_title("Canny")

fig.tight_layout()
plt.show()