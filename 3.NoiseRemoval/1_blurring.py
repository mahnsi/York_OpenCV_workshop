"""
Applying different types of blurring techniques in OpenCV to reduce noise and smoothen the image.
"""

import cv2 as cv

# Read image
img = cv.imread("cat1.png")

# Apply different blurring techniques:
# 1. Simple Average Blur - each pixel is replaced by the average of its neighborhood
blurred_img = cv.blur(src=img, ksize=(7, 7))

# 2. Gaussian Blur - advanced blurring technique that applies a Gaussian function to calculate the 
# weights for each pixel in the neighborhood, giving more importance to pixels closer to the center. 
g_img = cv.GaussianBlur(src=img, ksize=(7, 7), sigmaX=10) # sigmaX controls the spread of the Gaussian function in the x-direction, influencing the amount of blur (in this case, sigmaX=10).

# 3. Median Blur - replaces each pixel with the median value in its neighborhood, reducing salt-and-pepper noise
m_img = cv.medianBlur(src=img, ksize=7)

# Display the results
cv.imshow("Simple Blur", blurred_img)
cv.imshow("Gaussian Blur", g_img)
cv.imshow("Median Blur", m_img)

cv.waitKey(0)
cv.destroyAllWindows()


"""
# Notes:

- Intuition: Blurring reduces fine details by averaging neighboring pixels, leading to smoother, less detailed images.
- Different blurring techniques use various mathematical approaches to calculate the neighborhood average, depending on the use case.

1. Simple Average Blur (cv.blur)
Explanation: Simple Average Blur, or simply "average blur," is a basic blurring technique where each pixel is replaced by the average of all the pixels in a specified neighborhood. In the code, the ksize parameter (7, 7) defines the neighborhood as a 7x7 pixel area.
How it works: For each pixel in the image, OpenCV takes the average of all the pixels within the 7x7 kernel centered around that pixel. The resulting pixel value is then assigned to the center pixel, smoothing the image by reducing abrupt intensity changes.
Use cases: Average blur is generally used for simple noise reduction or smoothing, but it can create overly soft images and doesn’t handle more complex noise (e.g., salt-and-pepper noise) as effectively.

2. Gaussian Blur (cv.GaussianBlur)
Explanation: Gaussian Blur is an advanced blurring technique that applies a Gaussian function to calculate the weights for each pixel in the neighborhood, giving more importance to pixels closer to the center. This produces a natural-looking blur, as pixels closer to the center have a higher influence on the blur result.
Parameters:
ksize specifies the size of the kernel (in this case, a 7x7 kernel).
sigmaX controls the spread of the Gaussian function in the x-direction, influencing the amount of blur (in this case, sigmaX=10).
How it works: The Gaussian function calculates weights based on the distance from the center of the kernel. Pixels nearer to the center have higher weights, while those further away have less influence. This weighting creates a gradual blur effect.
Use cases: Gaussian Blur is commonly used for reducing Gaussian (random) noise in images while preserving edges better than average blur. It’s also widely used for creating a "soft" focus effect in photography.

3. Median Blur (cv.medianBlur)
Explanation: Median Blur replaces each pixel's value with the median value of all the pixels in its kernel neighborhood. Unlike average blur, which calculates the mean, median blur uses the median, making it highly effective at removing "salt-and-pepper" noise.
Parameters:
ksize defines the size of the neighborhood. Here, it is set to 7, so each pixel will be replaced by the median of a 7x7 neighborhood.
How it works: The median filter sorts all pixel values within the kernel and then selects the middle (median) value as the new pixel value. This approach is particularly effective at preserving edges and reducing the impact of outlier noise, such as single bright or dark pixels (salt-and-pepper noise).
Use cases: Median blur is ideal for removing salt-and-pepper noise (isolated, contrasting pixels), making it useful in images with impulse noise. It’s commonly used in preprocessing stages for image segmentation or object detection.
"""