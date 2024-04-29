import mediapipe as mp
import cv2
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Open video capture from camera
cap = cv2.VideoCapture(0)

# Create hand recognition model with higher min_detection_confidence for accuracy
with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    print('Press "q" to exit')
    while cap.isOpened():
        # Read each frame
        ret, frame = cap.read()

        # MediaPipe processing
        # Convert BGR to RGB for MediaPipe processing
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Detect hands in the frame
        results = hands.process(image)

        # Convert back to BGR for display
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Draw hand landmarks if hands are detected
        if results.multi_hand_landmarks:
            for num, hand_landmarks in enumerate(results.multi_hand_landmarks):
                # Draw landmarks and connections as before
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                         mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                         mp_drawing.DrawingSpec(color=(121, 44, 250), thickness=2, circle_radius=2))

                # Thumb tip and wrist landmarks
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]

                # Check thumb position (adjusted for both hands)
                if (thumb_tip.x < wrist.x and num == 0) or (thumb_tip.x > wrist.x and num == 1):
                    is_thumbs_up = True

                    # Check fingertip distances (optional, adjust threshold as needed)
                    finger_landmarks = [mp_hands.HandLandmark.INDEX_FINGER_TIP,
                                        mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
                                        mp_hands.HandLandmark.RING_FINGER_TIP,
                                        mp_hands.HandLandmark.PINKY_TIP]
                    distance_threshold = 50  # Adjust this based on your setup
                    for finger_tip in finger_landmarks:
                        fingertip_landmark = hand_landmarks.landmark[finger_tip]
                        base_landmark = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST + finger_tip - mp_hands.HandLandmark.INDEX_FINGER_TIP]
                        distance = np.linalg.norm(fingertip_landmark, base_landmark)
                        if distance > distance_threshold:
                            is_thumbs_up = False
                            break  # Stop checking fingers if one isn't curled

                    # Display message based on curled fingers and thumb position
                    if is_thumbs_up:
                        cv2.putText(image, f'Thumbs Up! (Hand #{num+1})', (10, 30),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    else:
                        cv2.putText(image, f'Not a Thumbs Up (Hand #{num+1})', (10, 30),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)  # Blue text

        # Render the frame with hand landmarks and detection message (if any)
        cv2.imshow('Hand Tracking with Thumbs Up Detection', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

# Release resources
cap.release()
cv2.destroyAllWindows()
