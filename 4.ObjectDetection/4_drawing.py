# ================================
# Drawing Shapes on an Image
# ================================
# This script demonstrates how to draw various shapes (line, rectangle, circle) and text 
# on an image using OpenCV.

import cv2 as cv
import _Colors_module as c


# Read 
img = cv.imread("wb.png")
# you may need to resize the img!

# Resize Image
img = cv.resize(src=img, dsize=(img.shape[1]//2, img.shape[0]//2))

# Shape of the image (height, width, channels)
print(f"Image Shape: {img.shape}")

# ================================
# Drawing a Line
# ================================
# cv.line(image, start_point, end_point, color, thickness)
# Draw a line from point (500, 950) to (1000, 850) with a magenta color and thickness of 6.
cv.line(img=img, pt1=(500, 300), pt2=(1000, 500), color=c.MAGENTA, thickness=6)

# ================================
# Drawing a Rectangle
# ================================
# cv.rectangle(image, top_left, bottom_right, color, thickness)
# Draw a filled red rectangle from point (600, 550) to (1040, 800) by setting thickness=-6.
# The negative thickness means the rectangle will be filled.
cv.rectangle(img=img, pt1=(200, 300), pt2=(300, 450), color=c.RED, thickness=-6)

# ================================
# Drawing a Circle
# ================================
# cv.circle(image, center, radius, color, thickness)
# Draw a blue circle centered at (1000, 900) with a radius of 60 and a thickness of 4.
cv.circle(img=img, center=(400, 400), radius=30, color=c.BLUE, thickness=-1)

# ================================
# Adding Text
# ================================
# cv.putText(image, text, origin, fontFace, fontScale, color, thickness)
# Add the text "This is a text" at position (1700, 1000) with a font size of 2 and black color.
cv.putText(img=img, text="This is a text", org=(200, 250), fontFace=5, fontScale=2, color=c.BLACK, thickness=3)

# Display
cv.imshow("Drawings on Image", img)
cv.waitKey(0)
cv.destroyAllWindows()






# ================================
# Note:
# ================================
# - **Line**: A simple line can be drawn by defining two points and setting the desired color and thickness.
# - **Rectangle**: A rectangle is defined by its top-left and bottom-right corner. A negative thickness will fill the shape.
# - **Circle**: Circles are defined by their center, radius, color, and thickness.
# - **Text**: Text can be added at any location on the image using a specific font style and size.
# 
# **Coordinate System**:
# - The coordinate system in OpenCV images is (0, 0) at the top-left corner of the image.
# - The x-axis increases from left to right, and the y-axis increases from top to bottom.
#
# **Note**:
# - The colors (e.g., `MAGENTA`, `RED`, `BLUE`, `BLACK`) are likely defined in your custom `_Colors_module.py`.


# Axis:
################ x
# 0 1 2 3 4 5 6 
# 1 
# 2
# 3
# 4
# 5
# 6
# 
# y