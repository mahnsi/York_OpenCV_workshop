"""
Applying different types of blurring techniques in OpenCV to reduce noise and smoothen the image.
"""

import cv2 as cv

# Read image
img = cv.imread("cat1.png")

# Apply different blurring techniques:
# 1. Simple Average Blur - each pixel is replaced by the average of its neighborhood
blurred_img = cv.blur(src=img, ksize=(7, 7))

# 2. Gaussian Blur - applies a weighted average where pixels closer to the center have more influence
g_img = cv.GaussianBlur(src=img, ksize=(7, 7), sigmaX=10)

# 3. Median Blur - replaces each pixel with the median value in its neighborhood, reducing salt-and-pepper noise
m_img = cv.medianBlur(src=img, ksize=7)

# Display the results
cv.imshow("Simple Blur", blurred_img)
cv.imshow("Gaussian Blur", g_img)
cv.imshow("Median Blur", m_img)

cv.waitKey(0)
cv.destroyAllWindows()





# Notes:
# - Blurring is useful for reducing noise in images.
# - Different blurring functions:
#   1. **Simple Blur** (`cv.blur`): Averages pixel values in the specified kernel size (7x7 here), providing a straightforward smoothing.
#   2. **Gaussian Blur** (`cv.GaussianBlur`): Applies a Gaussian function to calculate weighted averages, often more natural for images.
#   3. **Median Blur** (`cv.medianBlur`): Uses the median instead of the mean, effective in removing specific noise types like salt-and-pepper.

# - Intuition: Blurring reduces fine details by averaging neighboring pixels, leading to smoother, less detailed images.
# - Different blurring techniques use various mathematical approaches to calculate the neighborhood average, depending on the use case.
