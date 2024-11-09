"""
 This script demonstrates how to apply simple (global) thresholding to an image,
 converting it into a binary image. 
 The process includes grayscale conversion, thresholding, and (optional) noise reduction via blurring.
"""

import cv2 as cv

# Read the image
img = cv.imread("cat1.png")

# Convert the image to grayscale
# Thresholding works on grayscale images, where each pixel has only intensity information.
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Apply simple (global) thresholding
# Any pixel intensity below the threshold (80) becomes black (0), and above it becomes white (255).
# This converts the image into a binary image (black and white).
ret, th_img = cv.threshold(src=gray_img, thresh=80, maxval=255, type=cv.THRESH_BINARY)

# optional: Apply median blur to remove noise
# Median blur helps smooth out the binary image by reducing small fluctuations.
blur_img = cv.medianBlur(th_img, 7)

# Display the results
cv.imshow("Thresholded Image", th_img)
cv.imshow("Blurred Image", blur_img)
cv.waitKey(0)




# ================================
# Note:
# ================================
# 1. **Thresholding**:
# - Simple thresholding is a technique used to convert a grayscale image into a binary image.
# - The pixel intensity is compared to a specified threshold, and based on the result, 
#   the pixel is set to either black or white.

# 2. **Thresholding Types**:
# - **Simple (Global) Thresholding**: A single threshold value is applied across the entire image.
#   - Works well for images with uniform lighting conditions.
#   - Can lead to poor results with varying lighting across the image.
# - **Adaptive Thresholding**: Different thresholds are computed for smaller regions in the image.
#   - It is more effective for images with varying lighting conditions.

# 3. **Use Cases**:
# - **Semantic Segmentation**: Helps divide an image into regions (e.g., object vs. background).
# - **Object Detection and Shape Analysis**: Thresholding can help identify and isolate objects from the background.
# - **OCR (Optical Character Recognition)**: Converts scanned text into machine-readable text by segmenting characters from the background.

# 4. **Image Noise Reduction**:
# - After thresholding, noise can appear due to minor pixel variations. 
#   Applying a **median blur** helps smooth the image and reduce this noise.

