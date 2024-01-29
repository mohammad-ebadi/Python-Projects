# Volume Change With Hand Movement
# first of all you have to type " pip install opencv-python 
# & then type "pip install mediapipe"
import cv2
import mediapipe as mp
import math
import numpy as np
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
#volume.GetMute()
#volume.GetMasterVolumeLevel()
#volume.GetVolumeRange()
volume.SetMasterVolumeLevel(-20.0, None)

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()

while True:
    success , img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:

        hand = results.multi_hand_landmarks[0]

        mp.solutions.drawing_utils.draw_landmarks(img , hand , mpHands.HAND_CONNECTIONS)


        lmList = []
        for id , lm in enumerate(hand.landmark):
            
            h , w , c =img.shape
            cx , cy = int(lm.x * w), int(lm.y * h)
            lmList.append([id , cx , cy])

        if len(lmList) > 0:
            x1 , y1 =lmList[4][1] , lmList[4][2]
            x2 , y2 =lmList[8][1] , lmList[8][2]
            cx , cy =(x1 + x2) // 2 , (y1 + y2) // 2

            cv2.circle(img , (x1 , y1), 10 , (255,255,0), cv2.FILLED)
            cv2.circle(img , (x2 , y2), 10 , (255,255,0), cv2.FILLED)
            cv2.circle(img , (cx , cy), 10 , (255,255,0), cv2.FILLED)
            cv2.line(img , (x1 , y1),(x2 , y2 ),(255,255,0),3)

            length = int(math.hypot(x2 - x1 , y2 - y1))

            handRange = [50 , 300]

            vol = int(np.interp(length , handRange , [-64, 0]))

            volume.SetMasterVolumeLevel(vol, None)

            #print(length)

    cv2.imshow("Image",img)
    cv2.waitKey(1)
