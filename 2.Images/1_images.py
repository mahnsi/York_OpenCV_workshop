"""
Reading and displaying an image using OpenCV.
"""

import cv2 as cv

# Read the image from the specified path 
# (Note: Make sure you navigate to the "2. Images" folder before running the code)
img = cv.imread("cat1.png")

# Display the image in a window ("Cat1" is the name of the window)
cv.imshow("Cat1", img)

# Wait indefinitely until a key is pressed. (e.g cv.waitKey(1000) - waits 1000ms which is 1 second)
cv.waitKey(0)

# Close all OpenCV windows after a key press.
cv.destroyAllWindows()


# # Reading and displaying (better way)
# img = cv.imread("cat1.png")
# if img is None:
#     print("Error: Could not load image. Check the file path.")
# else:
#     cv.imshow("Cat1", img)
#     cv.waitKey(0)
#     cv.destroyAllWindows()