# gesture_control.py
"""
Gesture Control for Prosthetic Arm using OpenCV + MediaPipe + STM32
Author: Aryaman
"""

import cv2
import mediapipe as mp
import serial
import time

# -----------------------------
# Configuration
# -----------------------------
SERIAL_PORT = "COM3"  # Change to '/dev/ttyUSB0' for Linux
BAUD_RATE = 115200
DEBUG = True

# Initialize UART serial
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)
    print("[INFO] Connected to STM32 via UART")
except Exception as e:
    print(f"[ERROR] Could not open serial port: {e}")
    ser = None

# Mediapipe Hand Detection
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# -----------------------------
# Gesture Recognition Logic
# -----------------------------
def recognize_gesture(hand_landmarks):
    """
    Very basic rule-based gesture recognition.
    You can extend this using ML models if needed.
    """
    thumb_tip = hand_landmarks.landmark[4].y
    index_tip = hand_landmarks.landmark[8].y
    middle_tip = hand_landmarks.landmark[12].y
    ring_tip = hand_landmarks.landmark[16].y
    pinky_tip = hand_landmarks.landmark[20].y
    palm_y = hand_landmarks.landmark[0].y

    # Example gestures
    if index_tip < palm_y and middle_tip < palm_y:
        return "OPEN"   # Open hand
    elif index_tip > palm_y and middle_tip > palm_y:
        return "FIST"   # Closed fist
    else:
        return "UNKNOWN"

# -----------------------------
# Main Loop
# -----------------------------
cap = cv2.VideoCapture(0)

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7) as hands:
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("[ERROR] Failed to capture frame")
            break

        # Flip for mirror effect
        frame = cv2.flip(frame, 1)

        # Convert BGR → RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process hands
        results = hands.process(rgb_frame)

        gesture = "NONE"

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                gesture = recognize_gesture(hand_landmarks)

        # Send command to STM32
        if ser and gesture in ["OPEN", "FIST"]:
            ser.write((gesture + "\n").encode())

        # Debug info
        if DEBUG:
            cv2.putText(frame, f"Gesture: {gesture}", (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Show video
        cv2.imshow("Gesture Control", frame)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC key to exit
            break

cap.release()
cv2.destroyAllWindows()
if ser:
    ser.close()
