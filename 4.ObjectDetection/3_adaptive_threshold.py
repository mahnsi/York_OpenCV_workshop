import cv2 as cv
import os

# ================================
# Adaptive Thresholding Example
# ================================
# This script demonstrates how to apply adaptive thresholding to an image. 
# Unlike simple thresholding, adaptive thresholding calculates a different threshold 
# for each region of the image, making it more effective for images with varying lighting conditions.

# this is how they scan documents and convert them to black and white
# useul for OCR (opticall character recognition)

# Read 
img = cv.imread("note.webp")

# Convert the image to grayscale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

"""
Apply adaptive thresholding
Adaptive thresholding calculates a threshold for each pixel based on the values in its neighborhood.
In this case, we use a Gaussian mean to compute the threshold.
The parameters are:
- 255: The maximum intensity value (white).
- cv.ADAPTIVE_THRESH_GAUSSIAN_C: The method for computing the threshold (Gaussian weighted sum of neighborhood values).
- cv.THRESH_BINARY: The type of thresholding (binary thresholding).
- 21: The size of the neighborhood region (21x21 pixels) used to calculate the threshold for each pixel.
- 30: A constant value subtracted from the computed mean. This helps fine-tune the threshold, making it more sensitive to specific pixel intensities.
"""

th_img = cv.adaptiveThreshold(src=gray_img, maxValue=255, adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType=cv.THRESH_BINARY, blockSize=21, C=30)

# Optionally, you can apply noise removal (e.g., median blur), but for now its not needed
# blur_img = cv.medianBlur(th_img, 7)

# Display
cv.imshow("Thresholded Image", th_img)
cv.waitKey(0)
cv.destroyAllWindows()








# ================================
# Note:
# ================================
# 1. **Types of Thresholding**:
# - **Simple Thresholding**: Applies a fixed threshold to the entire image.
#   - Suitable for images with uniform lighting.
#   - Simple and fast but ineffective for images with uneven lighting.
# - **Adaptive Thresholding**: Computes a threshold for each pixel based on local neighborhood values.
#   - Effective for images with varying lighting conditions or shadows.
#   - More computationally expensive but produces better results for complex images.

# 2. **Use Cases**:
# - **Semantic Segmentation**: Segments an image into different regions (e.g., separating the subject from the background).
#   - Adaptive thresholding works better for images with varying light conditions.
# - **OCR (Optical Character Recognition)**: Adaptive thresholding helps in improving text recognition from images by converting the image into a binary format.
#   - Helps OCR algorithms to distinguish text from the background more effectively.

# 3. **Intuition**:
# - **Thresholding** is used to convert a grayscale image into a binary image by setting pixels either to black or white based on their intensity.
# - Simple thresholding applies one threshold to the entire image, while adaptive thresholding considers local regions to determine different thresholds for different areas of the image.

# 4. **Noise Reduction**:
# - After thresholding, noise can appear due to minor pixel variations. 
#   - In such cases, median blur or other filtering techniques can help remove noise and enhance the quality of the binary output.
