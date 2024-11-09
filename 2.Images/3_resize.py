"""
Resizing an image to specified dimensions and displaying it.
"""

import cv2 as cv

# Read 
img = cv.imread("cat2.png")

# Resize the image to specified width and height (650x500)
# Note: Resizing may distort the image if the aspect ratio is not preserved
resized_img = cv.resize(src=img, dsize=(650, 650))

print("Original Image Shape:", img.shape)
print("Resized Image Shape:", resized_img.shape)

# Display images
cv.imshow("Original Image", img)
cv.imshow("Resized Image", resized_img)

cv.waitKey(0)
cv.destroyAllWindows()

"""
Note: You can't directly set the display size of `cv.imshow` windows. 
To control the display size, you need to resize the image itself using `cv.resize`.
"""