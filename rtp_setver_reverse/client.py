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



s = socket(AF_INET, SOCK_STREAM) # create TCP socket 
s.connect(addr)

while True:
    

    data = None
    data = s.recv(921600)
    receive_data = np.frombuffer(data, dtype='uint8')
    r_img = cv2.imdecode(receive_data, 1)
    cv2.putText(r_img, "server", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow('server', r_img)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

s.close()
cv2.destroyAllWindows()