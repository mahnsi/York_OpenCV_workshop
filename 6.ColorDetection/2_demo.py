import cv2 as cv
from _util import get_limits  # Function to obtain color limits in HSV
from PIL import Image  # For converting mask to PIL format to get bounding box
import _colors_module as c  # Custom module for color definitions

# ================================
# Webcam Color Detection with Bounding Box
# ================================
# This script captures video from the webcam, detects areas with a specific color
# (e.g., yellow), and draws a bounding box around them.
# Press 'q' to exit the video display.

# Step 1: Open the webcam
webcam = cv.VideoCapture(index=0)

# Capture frames continuously
while True:
    # Step 2: Capture a frame from the webcam
    ret, frame = webcam.read()

    # Step 3: Convert the frame from BGR to HSV color space
    hsv_img = cv.cvtColor(src=frame, code=cv.COLOR_BGR2HSV)
    # Step 4: Get the HSV color range for the target color (e.g., yellow)
    lowerLimit, upperLimit = get_limits(color=c.YELLOW)

    # Step 5: Create a mask to isolate the specified color range in the frame
    mask = cv.inRange(src=hsv_img, lowerb=lowerLimit, upperb=upperLimit)
    
    # Step 6: Convert the mask (numpy array) to a PIL image for easy bounding box extraction
    mask_ = Image.fromarray(mask)
    # Step 7: Get the bounding box for the detected color area
    bbox = mask_.getbbox()

    # Step 8: Draw a bounding box if the color is detected in the frame
    if bbox:
        x1, y1, x2, y2 = bbox
        cv.rectangle(img=frame, pt1=(x1, y1), pt2=(x2, y2), color=c.GREEN, thickness=4)

    # Step 9: Display the frame with the bounding box
    cv.imshow(winname="webcam", mat=frame)
    if cv.waitKey(delay=1) & 0xFF == ord("q"):
        break

# Release resources
webcam.release()
cv.destroyAllWindows()

# ================================
# Notes:
# ================================
# - **Step 1**: Initializes the webcam for capturing frames.
# - **Step 2**: Reads each frame in the loop for processing.
# - **Step 3**: Converts the frame to HSV, making it easier to filter by color.
# - **Step 4**: Uses `get_limits` to obtain the HSV color range for yellow.
# - **Step 5**: Creates a mask to identify areas in the image that match the color range.
# - **Step 6**: Converts the mask to a PIL Image to extract the bounding box.
# - **Step 7**: Extracts the bounding box around detected color areas in the mask.
# - **Step 8**: Draws the bounding box on the frame to indicate detected color areas.
# - **Step 9**: Displays the processed frame with bounding boxes in a window.
# - **Step 10**: Allows the user to press 'q' to stop the loop and close the display.
# - **Step 11**: Releases the webcam and closes all OpenCV windows.
