import cv2
import mediapipe as mp
import pyautogui as py
cap=cv2.VideoCapture(0)
hand_detector=mp.solutions.hands.Hands()
drawing_utils=mp.solutions.drawing_utils
screen_width,screen_height=py.size()
x1=0
y1=0
while True:
    _,frame=cap.read()
    frame_height,frame_width,_=frame.shape
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output=hand_detector.process(rgb_frame)
    hands=output.multi_hand_landmarks


    if hands:
        for hand in hands:
            landmarks=hand.landmark
            for id,landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                if id==8:
                    cv2.circle(img=frame,center=(x,y),thickness=2,radius=2,color=(163,3,27))
                    x1 = int(x * (screen_width / frame_width))
                    y1 = int(y * (screen_height / frame_height))
                    py.moveTo(int(x*(screen_width/frame_width)),int(y*(screen_height/frame_height)))

    cv2.imshow("virtual mouse",frame)
    cv2.waitKey(1)