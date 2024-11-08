"""
Demo: Noise Reduction Using Various Blurring Techniques

This demo shows how blurring can help reduce noise in images. 
We will use three different types of blurring techniques to smooth the image:
1. Simple Averaging (cv.blur)
2. Gaussian Blurring (cv.GaussianBlur)
3. Median Blurring (cv.medianBlur)
"""

import cv2 as cv
import os

# path
path = os.path.join(".", "3.Noise Removel", "noisyImg.png")

# Read the image
img = cv.imread(path)


# 1. Simple Average Blur:
blurred_img = cv.blur(img, (7, 7))

# 2. Gaussian Blur: 
g_img = cv.GaussianBlur(img, (7, 7), 3)

# 3. Median Blur: 
m_img = cv.medianBlur(img, 7)

# Display the original and blurred images
cv.imshow("Original Image", img)
cv.imshow("Averaging Blur", blurred_img)
cv.imshow("Gaussian Blur", g_img)
cv.imshow("Median Blur", m_img)
cv.waitKey(0)

