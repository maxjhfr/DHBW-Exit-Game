import mediapipe as mp
import cv2
import numpy as np
from math import atan2, degrees

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


#open video from camera
cap = cv2.VideoCapture(0)


#create hand recognition model
with mp_hands.Hands(max_num_hands = 1, min_detection_confidence = 0.7, min_tracking_confidence = 0.5) as hands:

  print('press "q" to exit')
  while cap.isOpened():
    #read every frame 
    ret, frame = cap.read()

    #mediapipe recognition
    #feed from openCV is in BGR and needs to be set to RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False

    #detect
    results = hands.process(image)

    image.flags.writeable = True
    #back to BGR for displaying
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    #draw landmarks on camera feed one frame at the time
    if results.multi_hand_landmarks:

      thumb_up = False
      thumb_angle = False
      curled = []

      for num, hand in enumerate(results.multi_hand_landmarks):
        #draw landmarks and connections
        mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                  #make lines look pretty
                                  mp_drawing.DrawingSpec(color=(121, 22, 76), thickness = 2, circle_radius = 4),
                                  mp_drawing.DrawingSpec(color=(121, 44, 250), thickness = 2, circle_radius = 2),
                                  )


        #process if there is a "thumbs up"
        #thumbs up is if thumb is raised and others are curled
        thumb_tip = hand.landmark[mp_hands.HandLandmark.THUMB_TIP] 
        thumb_mcp = hand.landmark[mp_hands.HandLandmark.THUMB_MCP] 
        middle_finger_mcp = hand.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP]
        wrist = hand.landmark[mp_hands.HandLandmark.WRIST]
        other_tips = [mp_hands.HandLandmark.INDEX_FINGER_TIP,
                      mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
                      mp_hands.HandLandmark.RING_FINGER_TIP,
                      mp_hands.HandLandmark.PINKY_TIP]
        other_mcp = [mp_hands.HandLandmark.INDEX_FINGER_MCP,
                      mp_hands.HandLandmark.MIDDLE_FINGER_MCP,
                      mp_hands.HandLandmark.RING_FINGER_MCP,
                      mp_hands.HandLandmark.PINKY_MCP]
        

        #check if thumb is pointing up (rotation)
        angle_radians = atan2(thumb_mcp.y - thumb_tip.y,
                              thumb_mcp.x - thumb_tip.x)
        angle_degrees = degrees(angle_radians)

        # Adjust angle to the range 0 to 360 degrees
        if angle_degrees < 0:
            angle_degrees += 360

        if 60 <= angle_degrees <= 120:
          thumb_angle = True





        # thumb is over other tips
        if hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < thumb_tip.y:
          thumb_up = False
        else:
          thumb_up = True
        
        
        #check distance between other tips and wrist (check if curled)
        for i in range(len(other_tips)):
          finger_tip_landmark = hand.landmark[other_tips[i]] 
          finger_mcp_landmark = hand.landmark[other_mcp[i]] 

          middle_point = ([(wrist.x + finger_mcp_landmark.x) / 2, 
                                      (wrist.y + finger_mcp_landmark.y) / 2,
                                      (wrist.z + finger_mcp_landmark.z) / 2])

          finger_point = np.array([finger_tip_landmark.x, finger_tip_landmark.y, finger_tip_landmark.z])
          distance = np.linalg.norm(middle_point - finger_point)

          if distance > 0.1:
            curled.append(False)
          else:
            curled.append(True)



        #calculate if is thubs up
        curled_true = sum(curled)  
        curled_false = len(curled) - curled_true
        
        total_elements = len(curled)
        if total_elements == 0:
          break
        percent_true = (curled_true / total_elements) * 100 
        percent_false = (curled_false / total_elements) * 100

        print("True:  ", percent_true, "  False:   ", percent_false, "   ", curled, "   ", thumb_up, "   ", thumb_angle)

        #if thumb up, then show text
        if percent_true > 80 and thumb_up and thumb_angle:
          cv2.putText(image, f'Daumen hoch!', (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                      1, (144, 255, 0), 2)

    


    #render image from mediapipe
    cv2.imshow('Hand Tracking', image)

    if cv2.waitKey(10) & 0xFF == ord('q'):
      break

  cap.release()
  cv2.destroyAllWindows()



