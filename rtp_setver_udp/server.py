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

s.setblocking(0) # set to non blocking mode

while True:
    data = None
    try:
        data, _ = s.recvfrom(921600)
        receive_data = np.frombuffer(data, dtype='uint8')
        r_img = cv2.imdecode(receive_data, 1)

        cv2.putText(r_img, "server", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow('server', r_img)
    except BlockingIOError as e:
        pass

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()