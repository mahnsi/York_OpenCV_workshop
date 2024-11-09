import cv2 as cv

# ================================
# Webcam Video Capture, Flip, and Display
# ================================
# This script captures video from the default webcam (usually at index 0), mirrors the frames horizontally,
# and displays them in a window. Press 'q' to exit the video display.

# Initialize the webcam. Argument '0' selects the default webcam.
webcam = cv.VideoCapture(0)

while True:
    # Capture a frame from the webcam
    ret, frame = webcam.read()
    
    # Flip the frame horizontally (mirror effect)
    frame = cv.flip(src=frame, flipCode=1)
    
    # Display the mirrored frame in a window named "webcam"
    cv.imshow("webcam", frame)
    
    # Wait for 1 millisecond between frames to make it more responsive
    # Exit the loop if 'q' is pressed
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

# Release the webcam and close the window
webcam.release()
cv.destroyAllWindows()

# ================================
# Notes:
# ================================
# - **cv.flip()**: Flips the frame horizontally with `flipCode=1`, creating a mirror effect.
# - **cv.waitKey(1)**: Allows for smooth, fast display by updating the frame every 1 ms.
# - **Exit Condition**: Press 'q' to stop the loop and close the display.
# - **webcam.release() and cv.destroyAllWindows()**: Free resources and close OpenCV windows.
