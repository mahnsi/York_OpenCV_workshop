"""
Cropping an Image
"""

import cv2 as cv

# Read image
img = cv.imread("cat1.png")

# Print the shape of the image (height, width, channels) (BGR - 3 Channels)
print("Image shape:", img.shape)

# Crop the image
# Cropping syntax: img[y_start:y_end, x_start:x_end]
cropped_img = img[200:300, 100:500]


# Display Original Image
cv.imshow("Original Image", img)
# Display Cropped Image
cv.imshow("Cropped Image", cropped_img)

cv.waitKey(0) 
cv.destroyAllWindows()

"""
Note: Images are stored as NumPy arrays in OpenCV.

Each element in the numpy array represents a pixel.

Images contain a large amount of pixel data, and each pixel can hold values for color channels (e.g., RGB).
Storing images as NumPy arrays allows for efficient access and manipulation of pixel data using array slicing,
making tasks like cropping, filtering, and transformations straightforward and performant.

Regular arrays are not optimized for handling large-scale data processing. 
They lack the speed, flexibility, and memory efficiency of NumPy arrays, which are specifically designed for 
high-performance numerical operations.
"""