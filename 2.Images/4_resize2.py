"""
Resizing an image using a custom function.
"""

import cv2 as cv

def rescale(image, scale=0.75):
    # Images, Videos and Live Video
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(image, dimensions, interpolation=cv.INTER_AREA) 
    # interpolation=cv.INTER_AREA: This parameter specifies the interpolation method used for resizing.

# Reading Image
img = cv.imread("cat2.png")

# Resizing Image using our rescale function
resized_img = rescale(img)

# Print the shape of the image (height, width, channels) 
print("Original Image Shape:", img.shape)
print("Resized Image Shape:", resized_img.shape)

# Display images
cv.imshow("Original Image", img)
cv.imshow("Resized Image", resized_img)

cv.waitKey(0)
cv.destroyAllWindows()