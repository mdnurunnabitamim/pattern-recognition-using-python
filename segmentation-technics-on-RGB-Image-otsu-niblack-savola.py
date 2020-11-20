import matplotlib.pyplot as plt
from skimage import data, feature
from skimage.filters import (threshold_otsu, threshold_niblack, threshold_sauvola)
from skimage.color import rgb2gray

image = data.astronaut()
grayscale = rgb2gray(image)
edge = feature.canny(grayscale)
binary_global = grayscale > threshold_otsu(grayscale)
window_size = 25
thresh_niblack = threshold_niblack(grayscale, window_size=window_size, k=0.8)
thresh_sauvola = threshold_sauvola(grayscale, window_size=window_size)
binary_niblack = grayscale > thresh_niblack
binary_sauvola = grayscale > thresh_sauvola
plt.figure(figsize=(20, 15))

plt.subplot(2, 3, 1)
plt.imshow(image)
plt.title('Original')
plt.axis('off')
plt.subplot(2, 3, 2)
plt.imshow(grayscale, cmap=plt.cm.gray)
plt.title('greyscale')
plt.axis('off')
plt.subplot(2, 3, 3)
plt.title('Global Threshold')
plt.imshow(binary_global, cmap=plt.cm.gray)
plt.axis('off')
plt.subplot(2, 3, 4)
plt.imshow(binary_niblack, cmap=plt.cm.gray)
plt.title('Niblack Threshold')
plt.axis('off')
plt.subplot(2, 3, 5)
plt.imshow(binary_sauvola, cmap=plt.cm.gray)
plt.title('Sauvola Threshold')
plt.axis('off')

plt.show()
