import cv2
import time
import numpy as np
import handtrackingModule as htm
import math
import osascript

wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
pre_Time = 0
curr_Time = 0
cap.set(3, wCam)
cap.set(4, hCam)
minVol = 0
maxVol = 100
vol = 0
volBar = 400
volPer = 0
detector = htm.handDetector(detectionCon=0.9)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if len(lmList) != 0:
        # print(lmList[4], lmList[8])

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

        length = math.hypot(x2-x1, y2-y1)
        # print(length)

        vol = np.interp(length, [50, 210], [minVol, maxVol])
        volBar = np.interp(length, [50, 210], [400, 150])
        volPer = np.interp(length, [50, 210], [minVol, maxVol])
        print(int(length), vol)
        osascript.osascript(f"set volume output volume {vol}")
        if length < 50 :
            cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

        cv2.rectangle(img, (50,150), (85, 400), (0, 255, 0), 3)
        cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(volPer)), (50, 450), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)
    curr_Time = time.time()
    fps = 1 / (curr_Time - pre_Time)
    pre_Time = curr_Time

    # cv2.putText(img, f"FPS: {int(fps)}", (10, 40), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
