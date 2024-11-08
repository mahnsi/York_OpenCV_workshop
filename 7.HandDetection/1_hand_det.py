import cv2 as cv
import mediapipe as mp
import time

# ================================
# Hand Tracking with Mediapipe
# ================================
# This script captures video from the webcam, detects hands using Mediapipe, 
# and draws landmarks on detected hands. It also displays the FPS.
# Press 'q' to exit the video display.

# Step 1: Initialize the webcam
wc = cv.VideoCapture(0)

# Step 2: Set up Mediapipe hand-tracking module
mpHand = mp.solutions.hands  # Initializes MediaPipe's hand-tracking module.
hands = mpHand.Hands()  # Creates an instance of the hand detection and tracking model.

# Step 3: Set up Mediapipe drawing utility for landmarks
mpDraw = mp.solutions.drawing_utils

# Step 4: Initialize variables to calculate FPS
pTime = 0  # Previous time
cTime = 0  # Current time

# Step 5: Continuously capture frames from the webcam
while True:
    # Step 5.1: Read a frame from the webcam
    isSuccess, frame = wc.read()

    # Step 5.2: Convert the frame to RGB (Mediapipe expects RGB format)
    rgb_img = cv.cvtColor(src=frame, code=cv.COLOR_BGR2RGB)

    # Step 5.3: Process the RGB image with the hand-tracking model
    res = hands.process(rgb_img)
    
    # Step 6: Check if hands are detected
    if res.multi_hand_landmarks:
        # Step 6.1: Loop over each detected hand
        for handLms in res.multi_hand_landmarks:
            # Step 6.2: Loop over each landmark in the detected hand
            for id, lm in enumerate(handLms.landmark):
                height, width, chnls = frame.shape
                cx, cy = int(lm.x * width), int(lm.y * height)

                # Optional: Highlight specific landmarks (e.g., tips of index and middle fingers)
                if id == 8 or id == 12:
                    cv.circle(img=frame, center=(cx, cy), radius=40, color=(255, 255, 0), thickness=cv.FILLED)

            # Step 6.3: Draw landmarks and hand connections on the frame
            mpDraw.draw_landmarks(frame, handLms, mpHand.HAND_CONNECTIONS)

    # Step 7: Calculate and display the FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(img=frame, text=str(int(fps)), org=(10, 80),
               fontFace=cv.FONT_HERSHEY_COMPLEX, fontScale=3, color=(255, 0, 255), thickness=2)

    # Step 8: Display the frame
    cv.imshow("webcam", frame)
    
    # Step 9: Press 'q' to exit the display
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

# Step 10: Release resources and close the display window
wc.release()
cv.destroyAllWindows()

# ================================
# Notes:
# ================================
# - **Step 2**: Initializes the hand-tracking module for detecting and tracking hands.
# - **Step 5**: Reads frames in a loop to process each frame for hand detection.
# - **Step 6**: Extracts landmark positions and draws them on the frame.
# - **Step 7**: Calculates FPS to monitor performance.
# - **Exit Condition**: Press 'q' to stop the loop and close the display.
