import cv2 as cv
import mediapipe as mp
import time
from _handDetector_module import HandDetector  # Import custom HandDetector class

# ================================
# Hand Tracking with Custom HandDetector Class
# ================================
# This script uses a custom `HandDetector` class for hand tracking and landmark detection,
# capturing video from the webcam and drawing landmarks for specified finger points.
# Press 'q' to exit the video display.

def main():
    # Step 1: Initialize timing variables for calculating FPS
    pTime = 0  # Previous time
    cTime = 0  # Current time

    # Step 2: Open the webcam
    wc = cv.VideoCapture(0)

    # Step 3: Initialize the custom HandDetector class
    detector = HandDetector()

    # Step 4: Continuously capture frames from the webcam
    while True:
        # Step 4.1: Read a frame from the webcam
        isSuccess, frame = wc.read()

        # Step 5: Process the frame for hand detection
        detector.processHandImg(img=frame)       # Detect hands in the frame
        detector.showLandMarks(img=frame)        # Draw landmarks on the frame
        lm_list = detector.getLandmarksPosByIndex(img=frame, index=[4, 8])  # Get positions of specific landmarks

        # Step 6: Print the landmark list (optional, for debugging purposes)
        print(lm_list)
        
        # Optional: Retrieve all landmark positions for the hand
        # lm_list = detector.getAllHandLandmarkPos(img=frame)
        # if len(lm_list) != 0:
        #     print(lm_list[8])  # Example: print position of landmark with ID 8 (index fingertip)

        # Step 7: Calculate and display FPS on the frame
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv.putText(img=frame, text=str(int(fps)), org=(10, 80),
                   fontFace=cv.FONT_HERSHEY_COMPLEX, fontScale=3, color=(255, 0, 255), thickness=2)

        # Step 8: Display the frame with landmarks and FPS
        cv.imshow("webcam", frame)
        
        # Step 9: Exit on pressing 'q'
        if cv.waitKey(1) & 0xFF == ord("q"):
            break

    # Step 10: Release resources and close the display window
    wc.release()
    cv.destroyAllWindows()

# Entry point of the script
if __name__ == "__main__":
    main()

# ================================
# Notes:
# ================================
# - **HandDetector**: A custom class that handles hand detection, drawing landmarks, and getting landmark positions.
# - **getLandmarksPosByIndex(index=[4, 8])**: Gets landmark positions by their IDs (e.g., 4 for thumb tip, 8 for index finger tip).
# - **FPS Display**: Shows FPS on the frame to monitor performance.
# - **Exit Condition**: Press 'q' to stop the loop and close the display.
