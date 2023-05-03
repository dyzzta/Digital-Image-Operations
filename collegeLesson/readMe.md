# Cheatsheet

* ## Morphological Transformations

Morfolojik dönüşümler, görüntü işlemede ve bilgisayarlı görü işlemede kullanılan bir dizi işlemdir. Bu işlemler, bir görüntünün şeklini ve yapısını değiştirerek gürültüleri kaldırmaya, özellikleri geliştirmeye ve nesneleri segmente etmeye yardımcı olur.
 
* ##### AŞINDIRMA(Erode)
* ##### YAYMA(dilate)  
* ##### Açma (Opening)
* ##### Kapama (Closing)
* ##### Morfolojik Gradyan

```python
import cv2
import numpy as np

# Load the image
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Define the structuring element
kernel = np.ones((3,3), np.uint8)

# Perform erosion and dilation operations
erosion = cv2.erode(img, kernel, iterations = 1)
dilation = cv2.dilate(img, kernel, iterations = 1)

# Perform opening and closing operations
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Compute the gradient of the image
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# Display the original and transformed images
cv2.imshow('Original Image', img)
cv2.imshow('Eroded Image', erosion)
cv2.imshow('Dilated Image', dilation)
cv2.imshow('Opened Image', opening)
cv2.imshow('Closed Image', closing)
cv2.imshow('Gradient Image', gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()

```