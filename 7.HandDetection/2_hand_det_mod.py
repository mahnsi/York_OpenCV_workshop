import cv2 as cv
import mediapipe as mp
import time
from _handDetector_module import HandDetector  # Import custom HandDetector class

# ================================
# Hand Tracking with Custom HandDetector Class
# ================================


def main():
    # Open the webcam
    wc = cv.VideoCapture(0)

    # Step 1: Initialize the custom HandDetector class
    detector = HandDetector()

    while True:
        _, frame = wc.read()

        # Step 5: Process the frame for hand detection
        detector.processHandImg(img=frame)       # Detect hands in the frame
        detector.showLandMarks(img=frame)        # Draw landmarks on the frame
        lm_list = detector.getLandmarksPosByIndex(img=frame, index=[4, 8,0])  # Get positions of specific landmarks

        # Step 6: Print the landmark list (optional, for debugging purposes)
        # print(lm_list)
        
        # Optional: Retrieve all landmark positions for the hand
        # lm_list = detector.getAllHandLandmarkPos(img=frame)
        # if len(lm_list) != 0:
        #     print(lm_list[8])  # Example: print position of landmark with ID 8 (index fingertip)

        # Display the frame with landmarks and FPS
        cv.imshow("webcam", frame)
        if cv.waitKey(1) & 0xFF == ord("q"):
            break

    # Step 10: Release resources and close the display window
    wc.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()

