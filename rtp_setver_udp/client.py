'''
Author: qishangxia OPO
Date: 2022-01-10 12:31:28
LastEditTime: 2022-01-14 14:51:00
LastEditors: CloudSir
Description: 
'''

import numpy as np
import cv2
from socket import *

#127.0.0.1 refers to the IP of the machine. It is used for testing. It needs to be changed to the IP of the server when in use
addr = ('127.0.0.1', 8081) 

cap = cv2.VideoCapture(0)

#Set the lens resolution, which is 640x480 by default
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

s = socket(AF_INET, SOCK_DGRAM) # create UDP socket SOCK_DGRAM

while True:
    _, img = cap.read()

    img = cv2.flip(img, 1)

    #Compressed picture
    _, send_data = cv2.imencode('.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 50])

    s.sendto(send_data, addr)
    print(f'sending data, size: {img.size} byte')

    cv2.putText(img, "client", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow('client', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

s.close()
cv2.destroyAllWindows()