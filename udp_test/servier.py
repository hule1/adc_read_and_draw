# -*- coding: utf-8 -*-
# @Author  : liuqi
# @Time    : 2023/3/24 13:00
# @Function:
import socket

UDP_IP = "127.0.0.1"  # 服务端IP地址
UDP_PORT = 5005  # 服务端端口号

# 创建UDP Socket并绑定IP地址和端口号
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

# 接收客户端发送的数据报
while True:
    data, addr = sock.recvfrom(1024)
    print("received message:", data.decode())
