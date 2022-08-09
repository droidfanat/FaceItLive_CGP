'''
Author: qishangxia OPO
Date: 2022-01-10 12:31:24
LastEditTime: 2022-01-14 14:52:54
LastEditors: CloudSir
Description: 
'''

import numpy as np
import cv2
from socket import *


s = socket (AF_INET, SOCK_STREAM) # create UDP socket
addr = ('0.0.0.0', 8081) # 0.0.0.0 indicates local
s.bind(addr)
s.listen(1)
conn, addr = s.accept()

cap = cv2.VideoCapture(0)

#Set the lens resolution, which is 640x480 by default
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    data = None
    try:
        _, img = cap.read()
        img = cv2.flip(img, 1)
    
        #Compressed picture
        _, send_data = cv2.imencode('.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 50])
        conn.sendall(send_data)
        print(f'sending data, size: {img.size} byte')
        cv2.putText(img, "client", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow('client', img)


    except BlockingIOError as e:
        pass

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()