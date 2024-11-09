"""A contour in image processing is a curve or a boundary that represents the outline of an object in an image. Contours are often used to detect and analyze the shapes and regions within an image, as they help identify the edges of objects. By converting an image to grayscale and then applying a binary threshold, we can separate objects from the background, allowing the contour-finding algorithm to detect these boundaries more accurately. In OpenCV, contours are typically used for object detection, image segmentation, and shape analysis, making them a valuable tool for a wide range of computer vision tasks."""

import _Colors_module as c
import cv2 as cv


# Read the image
birds = cv.imread("birds.jpg")

# Resize the image
birds = cv.resize(src=birds, dsize=(650, 650))

# Original Image after Resizing
cv.imshow("Original Image", birds)

# ================================
# Step 1: Convert to Grayscale pixels
# ================================
g_birds = cv.cvtColor(src=birds, code=cv.COLOR_BGR2GRAY)

# ================================
# Step 2: Thresholding
# ================================
# Threshold the grayscale image to get a binary image
# You can change the threshold value as needed
ret, th_birds = cv.threshold(src=g_birds, thresh=120, maxval=255, type=cv.THRESH_BINARY_INV)

# ================================
# Optional Step: Blur the Image (if needed to reduce noise)
# ================================
# Applying a Gaussian blur to reduce noise before finding contours
# This can be helpful if there are small unwanted contours
blurred_birds = cv.GaussianBlur(th_birds, (5, 5), 1)

# ================================
# Step 3: Find Contours
# ================================
contours, _ = cv.findContours(image=blurred_birds, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_SIMPLE)

#Disply all contours
cv.drawContours(image=birds, contours=contours, contourIdx=-1, color=c.BLUE, thickness=3)
# contourIdx = -1 means draw all contours.

"""
Modes control the hierarchy and retrieval of contours:

cv.RETR_TREE: Retrieves all contours and reconstructs a full hierarchy, showing nested contours (like a tree structure).
cv.RETR_EXTERNAL: Retrieves only the outermost contours, ignoring any nested ones.
cv.RETR_LIST: Retrieves all contours without hierarchy, treating each contour independently.
cv.RETR_CCOMP: Retrieves contours and organizes them into two levels – outer and inner.

Methods define the contour approximation:
cv.CHAIN_APPROX_SIMPLE: Compresses horizontal, vertical, and diagonal segments, leaving only their endpoints, reducing memory usage.
cv.CHAIN_APPROX_NONE: Stores all contour points, giving a more detailed outline but using more memory.
"""

# ================================
# Display the Result
# ================================
cv.imshow("Detected Birds", birds)
cv.imshow("Blurred Birds", blurred_birds)

cv.waitKey(0)
cv.destroyAllWindows()


"""
Explanation of Steps:
1. Convert to Grayscale: Simplifies the image, making it easier to identify shapes.
2. Thresholding: Creates a binary image to isolate shapes/objects.
3. Find Contours: `cv.findContours()` detects contours based on binary regions.
4. Draw Contours: Draws detected contours on the original image for easy visualization.

Useful Link: https://aleksandarhaber.com/contour-detection-in-opencv-python-opencv-tutorial-in-python/
"""