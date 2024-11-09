"""
This script captures video from a webcam, applies a color mask to isolate specific colors, and displays the masked output in real-time.
Using OpenCV, it converts the video frames to HSV color space, applies a mask to isolate colors within specified HSV ranges (e.g., green or orange),
and displays the masked result.

The process includes:
1. Capturing frames from the webcam.
2. Converting frames from BGR to HSV.
3. Masking specific color ranges.
4. Displaying the masked video feed with the ability to quit by pressing "q".
"""

import cv2 as cv
import numpy as np
from _util import get_limits  # Function to obtain color limits in HSV
import _colors_module as c  # Custom module for color definitions

# Initialize webcam
webcam = cv.VideoCapture(index=0)

# Define HSV color ranges for masking specific colors
low_green = np.array([52, 52, 72])     # Lower HSV bound for green
high_green = np.array([102, 255, 255])  # Upper HSV bound for green
low_org = np.array([5, 50, 50])        # Lower HSV bound for orange
high_org = np.array([15, 255, 255])    # Upper HSV bound for orange

while True:
    # Capture a frame from the webcam
    ret, frame = webcam.read()
    if not ret:
        break

    # Convert the frame from BGR to HSV color space for easier color masking
    hsv_img = cv.cvtColor(src=frame, code=cv.COLOR_BGR2HSV)

    # Create a binary mask to isolate the specified color range in the frame (green here)
    mask = cv.inRange(src=hsv_img, lowerb=low_green, upperb=high_green) # works with hsv color

    # Steps to draw bounding boxes:
    # 1. opt: Convert the image to grayscale (if needed).
    # 2. opt: Apply thresholding to create a binary image (foreground as white, background as black).
    # 3. Use contours to detect boundaries of objects in the binary image.
    # 4. In a loop, for each contour, calculate the bounding box using cv.boundingRect().
    # 5. Draw the bounding box around each detected object on the original image.

    # Display the masked frame (showing only areas in the green color range)
    cv.imshow(winname="webcam", mat=mask)
    if cv.waitKey(delay=1) & 0xFF == ord("q"):
        break

# Release webcam and close OpenCV windows
webcam.release()
cv.destroyAllWindows()


"""
Binary Masking: Create a mask where desired areas are white (255) and others are black (0). 
Use cv2.bitwise_and() to apply the mask to the image.

ROI Masking: Define a rectangular region in the image. 
Create a mask for that region and apply it using cv2.bitwise_and().

Masking with Color Range: Use cv2.inRange() to create a mask based on a color range
(e.g., isolate specific colors in an image).
"""
