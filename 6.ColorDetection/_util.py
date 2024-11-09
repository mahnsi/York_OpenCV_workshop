"""
This script defines a function `get_limits(color)` that takes a BGR color as input and 
returns the lower and upper limits of the corresponding HSV range. This range is useful 
for creating masks based on color in the HSV color space.

The function handles the special case of the red hue, which has a wrap-around in the hue 
circle (0-180° in OpenCV). It ensures that both lower and upper HSV limits are set appropriately 
for color masking.

Parameters:
- color: A BGR color value (e.g., [255, 0, 0] for blue).
  
Returns:
- lowerLimit: The lower HSV limit for the given color.
- upperLimit: The upper HSV limit for the given color.
"""

import numpy as np
import cv2

def get_limits(color):
    # Convert the BGR color to HSV
    c = np.uint8([[color]])  # Convert input to an image format for cv2 conversion
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    hue = hsvC[0][0][0]  # Extract the hue value from the HSV color

    # Handle the hue wrap-around for the red color range
    if hue >= 165:  # Red hue at the upper end of the hue circle
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)  # Lower bound
        upperLimit = np.array([180, 255, 255], dtype=np.uint8)  # Upper bound (wrap around)
    elif hue <= 15:  # Red hue at the lower end of the hue circle
        lowerLimit = np.array([0, 100, 100], dtype=np.uint8)  # Lower bound (wrap around)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)  # Upper bound
    else:  # For other colors in the range
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)  # Lower bound
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)  # Upper bound

    return lowerLimit, upperLimit
