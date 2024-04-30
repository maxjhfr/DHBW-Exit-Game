import mediapipe as mp
import cv2
import numpy as np
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


#open video from camera
cap = cv2.VideoCapture(0)


#create hand recognition model
with mp_hands.Hands(min_detection_confidence = 0.7, min_tracking_confidence = 0.5) as hands:

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

      thumb_up = []
      curled = []

      for num, hand in enumerate(results.multi_hand_landmarks):
        #draw landmarks and connections
        mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                  #make lines look pretty
                                  mp_drawing.DrawingSpec(color=(121, 22, 76), thickness = 2, circle_radius = 4),
                                  mp_drawing.DrawingSpec(color=(121, 44, 250), thickness = 2, circle_radius = 2),
                                  )
        

        #process if there is a "thumbs up"


        #check if thumb is bent straight up




        #thumbs up is if thumb is raised and others are curled
        thumb_tip = hand.landmark[mp_hands.HandLandmark.THUMB_TIP] 
        wrist_landmark = hand.landmark[mp_hands.HandLandmark.WRIST]
        other_tips = [mp_hands.HandLandmark.INDEX_FINGER_TIP,
                      mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
                      mp_hands.HandLandmark.RING_FINGER_TIP,
                      mp_hands.HandLandmark.PINKY_TIP]
        
        #check if thumb is pointing up







        #check if thumb position is higher relative to wrist
        
        
        for finger_tip in other_tips:
          finger_tip_landmark = hand.landmark[finger_tip]

          # thumb is over other tips
          if finger_tip_landmark.y < thumb_tip.y:
            thumb_up.append(False)
          else:
            thumb_up.append(True)

          #check distance between other tips and wrist (check if curled)
          wrist_point = np.array([wrist_landmark.x, wrist_landmark.y, wrist_landmark.z])
          finger_point = np.array([finger_tip_landmark.x, finger_tip_landmark.y, finger_tip_landmark.z])

          distance = np.linalg.norm(wrist_point - finger_point)

          if distance > 0.15:
            thumb_up.append(False)
          else:
            thumb_up.append(True)


        




          

        #calculate percentage of thumb up
        num_true = sum(thumb_up)  
        num_false = len(thumb_up) - num_true

        
        total_elements = len(thumb_up)
        if total_elements == 0:
          break
        percent_true = (num_true / total_elements) * 100 
        percent_false = (num_false / total_elements) * 100

        print("True:  ", percent_true, "  False:   ", percent_false)


        #if thumb up, then show text
        if percent_true > 85 :
          cv2.putText(image, f'Daumen hoch!', (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                      1, (144, 255, 0), 2)

        





    #render image from mediapipe
    cv2.imshow('Hand Tracking', image)

    if cv2.waitKey(10) & 0xFF == ord('q'):
      break

  cap.release()
  cv2.destroyAllWindows()



