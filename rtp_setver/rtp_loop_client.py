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
addr_input_stream = ('127.0.0.1', 8081) 
addr_output_stream = ('127.0.0.1', 8082) 


s_input_stream = socket(AF_INET, SOCK_STREAM) # create TCP socket 
s_input_stream.connect(addr_input_stream)

s_output_stream = socket(AF_INET, SOCK_STREAM) # create UDP socket SOCK_DGRAM
s_output_stream.connect(addr_output_stream)


while True:
    

    data = None
    data = s_input_stream.recv(921600)
    receive_data = np.frombuffer(data, dtype='uint8')
    r_img = cv2.imdecode(receive_data, 1)
    cv2.putText(r_img, "retransleted", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    #Compressed picture
    _, send_data = cv2.imencode('.jpg', r_img, [cv2.IMWRITE_JPEG_QUALITY, 50])
    s_output_stream.send(send_data)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

s_input_stream.close()
s_output_stream.close()








