import cv2 as cv
import mediapipe as mp
import time

# ================================
# Hand Tracking with Mediapipe
# ================================

# Initialize the webcam
wc = cv.VideoCapture(0)

# Step 1: Set up Mediapipe hand-tracking module
mpHand = mp.solutions.hands  # Initializes MediaPipe's hand-tracking module.
hands = mpHand.Hands()  # Creates an instance of the hand detection and tracking model.

# Step 2: Set up Mediapipe drawing utility for landmarks
mpDraw = mp.solutions.drawing_utils

while True:
    # Read a frame from the webcam
    isSuccess, frame = wc.read()

    # Step 3: Convert the frame to RGB (Mediapipe expects RGB format)
    rgb_img = cv.cvtColor(src=frame, code=cv.COLOR_BGR2RGB)

    # Step 4: Process the RGB image with the hand-tracking model
    res = hands.process(rgb_img)
    
    # Step 5: Check if hands are detected
    if res.multi_hand_landmarks:
        # Loop over each detected hand
        for handLms in res.multi_hand_landmarks:
            # Loop over each landmark in the detected hand
            for id, lm in enumerate(handLms.landmark):
                height, width, chnls = frame.shape
                cx, cy = int(lm.x * width), int(lm.y * height)

                # Optional: Highlight specific landmarks (e.g., tips of index and middle fingers)
                if id == 8 or id == 12:
                    cv.circle(img=frame, center=(cx, cy), radius=40, color=(255, 255, 0), thickness=cv.FILLED)

            # Step 6: Draw landmarks and hand connections on the frame
            mpDraw.draw_landmarks(frame, handLms, mpHand.HAND_CONNECTIONS)


    # Display the frame
    cv.imshow("webcam", frame)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

# Step 10: Release resources and close the display window
wc.release()
cv.destroyAllWindows()

# ================================
# steps:
# ================================
# - **Step 2**: Initializes the hand-tracking module for detecting and tracking hands.
# - **Step 5**: Reads frames in a loop to process each frame for hand detection.
# - **Step 6**: Extracts landmark positions and draws them on the frame.
# - **Step 7**: Calculates FPS to monitor performance.
# - **Exit Condition**: Press 'q' to stop the loop and close the display.
