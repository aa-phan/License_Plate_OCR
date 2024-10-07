import cv2 as cv
import sys
import numpy as np

cap = cv.VideoCapture(0)

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    
    if not ret: 
        print("Can't receive frame, exiting...")
        break
    #frame = cv.flip(frame,0)
    #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', frame)
    out.write(frame)
    if(cv.waitKey(1) == ord('s')):
        break
    
cap.release()
out.release()
cv.destroyAllWindows()