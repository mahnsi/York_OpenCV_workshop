# ================================
# Demo - Object Detection using Contours - no masking
# ================================
# This demo shows how to detect objects in an image using contours in OpenCV.
# The process involves:
# 1. Converting the image to grayscale.
# 2. Applying a binary threshold to isolate objects.
# 3. Finding contours around the detected objects.
# 4. Drawing bounding boxes around the contours.
# 5. Displaying the image with detected objects outlined.
#
# This demo is useful for basic object detection and can be extended for
# various applications like shape detection, segmenting objects, etc.

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
# Step 4: Draw Contours and Bounding Boxes
# ================================
for cnt in contours:
    # Remove noisy contours based on area (filter small contours)
    if cv.contourArea(contour=cnt) > 200:
        # Draw contours on the original image
        cv.drawContours(image=birds, contours=cnt, contourIdx=-1, color=c.BLUE, thickness=3)

        # Get the bounding box for the CONTOUR
        x1, y1, w, h = cv.boundingRect(array=cnt) #calculates rectangle that can contain the contour cnt. (x1 and y1 represent the top-left corner coordinates of this bounding rectangle. w and h are the width and height of the rectangle, respectively.)
        # Draw the bounding box
        cv.rectangle(img=birds, pt1=(x1, y1), pt2=(x1 + w, y1 + h), color=c.YELLOW, thickness=3)
         

# ================================
# Display the Result
# ================================
cv.imshow("Detected Birds", birds)
cv.imshow("Blurred Birds", blurred_birds)

cv.waitKey(0)
cv.destroyAllWindows()



# ================================
# Notes:
# ================================
# 1. Grayscale: Converts the image to grayscale to simplify the contour detection process.
# 2. Threshold: A binary threshold is applied to isolate objects from the background.
# 3. Blurring: Optionally, apply Gaussian blur to reduce noise and smooth edges. This can help improve contour detection.
# 4. Contours: Using `cv.findContours()` to find contours in the binary image.
# 5. Bounding Boxes: For each detected contour, a bounding box is drawn around it.

# For more robust object detection, you can experiment with different threshold values, blurring techniques,
# or advanced techniques like edge detection (Canny).

# You're correct; this approach relies on a clear background to detect objects accurately.
# When the background is cluttered or the objects blend into it, contour detection using simple thresholding
# may not work well.