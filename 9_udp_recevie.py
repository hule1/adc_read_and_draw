# -*- coding: utf-8 -*-
# @Author  : liuqi
# @Time    : 2023/3/28 10:08
# @Function:
import socket

import numpy as np

UDP_IP = "127.0.0.1"  # Replace with the IP address of the sending machine
UDP_PORT = 12345  # Replace with the port used for sending data

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(4096)  # Buffer size is 4096 bytes
    import socket
    import numpy as np

    # 获取数据和数据标签
    message = np.fromstring(data.decode(), dtype=np.float32)
    if message.shape == (255,):
        message = np.reshape(tuple(message), (1,-1))

    # 处理数据
    for i in range(message.shape[0]):
        print(f"[{i}] : {message[i]:.5f}")