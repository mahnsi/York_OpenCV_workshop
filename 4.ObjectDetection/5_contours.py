import cv2 as cv

# ================================
# Step 1: Load and Display the Original Image
# ================================
image = cv.imread("cat1.png")  # Replace 'shapes.jpg' with your image file
cv.imshow("Original Image", image)

# ================================
# Step 2: Convert to Grayscale
# ================================
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# ================================
# Step 3: Apply Threshold to Convert to Binary
# ================================
_, binary_image = cv.threshold(gray_image, 127, 255, cv.THRESH_BINARY)
cv.imshow("Binary Image", binary_image)

"""
Thresholding Explanation:
    - Threshold Value: 127
    - Max Value: 255
    - THRESH_BINARY: Pixels > 127 are set to 255 (white), and pixels <= 127 are set to 0 (black).
"""

# ================================
# Step 4: Find Contours
# ================================
contours, _ = cv.findContours(binary_image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

"""
Contour Modes:
    - RETR_TREE: Retrieves all contours and organizes them in a hierarchical structure.
    - RETR_EXTERNAL: Retrieves only the outermost contours.
    
Contour Approximation Methods:
    - CHAIN_APPROX_SIMPLE: Saves memory by storing only the endpoints of contour segments.
    - CHAIN_APPROX_NONE: Stores all contour points (more detailed, but more memory-intensive).
"""

# ================================
# Step 5: Draw Contours on the Original Image
# ================================
contour_image = image.copy()
cv.drawContours(contour_image, contours, -1, (0, 255, 0), 2)  # Draw all contours in green with thickness of 2

# ================================
# Step 6: Display the Image with Contours
# ================================
cv.imshow("Contours", contour_image)
cv.waitKey(0)
cv.destroyAllWindows()
cv.destroyAllWindows()

"""
Explanation of Steps:
1. Convert to Grayscale: Simplifies the image, making it easier to identify shapes.
2. Thresholding: Creates a binary image to isolate shapes/objects.
3. Find Contours: `cv.findContours()` detects contours based on binary regions.
4. Draw Contours: Draws detected contours on the original image for easy visualization.
"""

