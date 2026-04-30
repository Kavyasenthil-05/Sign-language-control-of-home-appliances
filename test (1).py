import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import time
import serial

arduino = serial.Serial('COM8',9600)
time.sleep(2)

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

detector = HandDetector(maxHands=1)
classifier = Classifier("model/keras_model.h5","model/labels.txt")

offset = 20
imgSize = 300

folder = "dataset/E"
counter = 0

labels = ["A", "B", "C", "D", "E"]

last_sent = 0

while True:
    success, img = cap.read()
    imgOutput = img.copy()
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        x,y,w,h = hand['bbox']

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8)* 255
        imgCrop = img[max(0,y-offset):y+h+offset,max(0,x-offset):x+w+offset]
        
        imgCropShape = imgCrop.shape

        aspectRatio = h/w 

        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize - wCal) / 2)
            imgWhite[:, wGap:wCal+wGap] = imgResize
            prediction, index = classifier.getPrediction(imgWhite, draw=False)
            print(prediction, index)



        else:
            k = imgSize/w
            hCal = math.ceil(k*h)
            imgResize = cv2.resize(imgCrop,(imgSize, hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize-hCal)/2)
            imgWhite[hGap:hCal+hGap,:] = imgResize
            prediction, index = classifier.getPrediction(imgWhite, draw=False)

        if time.time() - last_sent >1:

            current_label = labels[index]
            print("Detected:", current_label)

            if current_label == "A":
                print("Sending A")
                arduino.write(b'A')

            elif current_label == "B":
                print("Sending B")
                arduino.write(b'B')

            elif current_label == "C":
                print("Sending C")
                arduino.write(b'C')

            elif current_label == "D":
                print("Sending D")
                arduino.write(b'D')

            elif current_label == "E":
                print("Sending E")
                arduino.write(b'E')
            
            last_sent = time.time()

        cv2.rectangle(imgOutput, (x-offset, y-offset-50), (x-offset+90, y-offset-50+50), (255, 0, 255), cv2.FILLED)
        
        cv2.putText(imgOutput, labels[index], (x,y-26), cv2.FONT_HERSHEY_COMPLEX, 1.7,(255, 255, 255),2)
        cv2.rectangle(imgOutput, (x-offset, y-offset), (x+w+offset, y+h+offset), (255, 0, 255), 4)

        cv2.imshow("ImageCrop", imgCrop)
        cv2.imshow("ImageWhite", imgWhite)


    cv2.imshow("Image",imgOutput)
    key = cv2.waitKey(1)
    
    if key == ord("q"):
        break
