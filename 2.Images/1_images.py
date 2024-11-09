"""
Read and display an image using OpenCV.
"""

import cv2 as cv

# Read the image from the specified path 
# (Note: Make sure you navigate to the "2. Images" folder before running the code)
img = cv.imread("cat1.png")

# Display the image in a window ("Cat1" is the name of the window)
cv.imshow("Cat1", img)

# Wait indefinitely until a key is pressed
cv.waitKey(0)

"""
import cv2 as cv
import os

# Define the path to the image file
# Use os.path.join for cross-platform compatibility
# img_path = os.path.join(".", "2.images", "cat1.png")

img_path = "cat1.png"
# If this path does not work, try setting img_path as a raw string, e.g., img_path = r"your_img_path"
# Alternative path example (for reference only, uncomment if needed)
# img_path = r"/Applications/STORAGE-1/york-hack/Demos/2.Images/cat1.png"

# Read the image from the specified path
img = cv.imread(img_path)

# Display the image in a window
cv.imshow("image frame", img)

# Wait indefinitely until a key is pressed
# Setting to 0 keeps the window open until a button is pressed
# Alternatively, set a delay in milliseconds (e.g., 5000 for 5 seconds)
cv.waitKey(0)

# Notes:
# - `cv.waitKey(0)` keeps the image window open until any key is pressed
# - To close automatically after a set time, replace `0` with a delay in milliseconds

"""
