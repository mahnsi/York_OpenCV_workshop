# ================================
# Demo - Object Detection using Contours
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

import os
import _Colors_module as c
import cv2 as cv

# Path
path = os.path.join(".", "4.Object Detection", "birds.jpg")


# Read the image
birds = cv.imread(path)


# ================================
# Step 1: Convert to Grayscale
# ================================
g_birds = cv.cvtColor(src=birds, code=cv.COLOR_BGR2GRAY)

# ================================
# Step 2: Thresholding
# ================================
# Threshold the grayscale image to get a binary image
# You can change the threshold value as needed
ret, th_birds = cv.threshold(src=g_birds, thresh=120, maxval=255, type=cv.THRESH_BINARY)

# ================================
# Optional Step: Blur the Image (if needed to reduce noise)
# ================================
# Applying a Gaussian blur to reduce noise before finding contours
# This can be helpful if there are small unwanted contours
blurred_birds = cv.GaussianBlur(th_birds, (5, 5), 0)

# ================================
# Step 3: Find Contours
# ================================
contours, _ = cv.findContours(image=blurred_birds, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_SIMPLE)

# ================================
# Step 4: Draw Contours and Bounding Boxes
# ================================
for cnt in contours:
    # Remove noisy contours based on area (filter small contours)
    if cv.contourArea(contour=cnt) > 200:
        # Draw contours on the original image
        cv.drawContours(image=birds, contours=cnt, contourIdx=-1, color=c.YELLOW, thickness=3)

        # Get the bounding box for the contour
        x1, y1, w, h = cv.boundingRect(array=cnt)
        # Draw the bounding box
        cv.rectangle(img=birds, pt1=(x1, y1), pt2=(x1 + w, y1 + h), color=c.YELLOW, thickness=3)

# ================================
# Display the Result
# ================================
cv.imshow("Detected Birds", birds)
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
