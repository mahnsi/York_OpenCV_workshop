"""
Demonstrating color space conversions in OpenCV, including BGR to RGB and grayscale.
"""

import cv2 as cv


# Read the image (default color space is BGR)
img = cv.imread("cat1.png")

# Convert color spaces
rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)     # BGR to RGB
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)   # BGR to Grayscale

# Display images in different color spaces
cv.imshow("Original (BGR)", img)          # Original in BGR
cv.imshow("RGB Image", rgb_img)           # Converted to RGB
cv.imshow("Grayscale Image", gray_img)    # Converted to Grayscale

cv.waitKey(0)
cv.destroyAllWindows()



# Notes:
# - OpenCV reads images in the BGR color space by default.
# - Color spaces are different ways to represent color information in an image:
#   1. **BGR**: The default format in OpenCV, with each pixel represented as Blue, Green, and Red channels.
#   2. **RGB**: Common format in other libraries, where each pixel is represented as Red, Green, and Blue channels.
#   3. **Grayscale**: Simplifies the image to a single channel, reducing information but lowering storage needs.
#   4. **HSV**: Often used in color detection and segmentation as it separates color intensity.

# - Converting from BGR to grayscale reduces the three color channels to one, making images lighter in storage and faster to process.
# - Each color space has unique applications; while some conversions may seem less meaningful to human eyes, they are valuable for computational tasks.
