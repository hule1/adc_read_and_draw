# -*- coding: utf-8 -*-
# @Author  : liuqi
# @Time    : 2023/3/24 13:00
# @Function:
import socket

UDP_IP = "127.0.0.1"  # 服务端IP地址
UDP_PORT = 5005  # 服务端端口号
MESSAGE = b"Hello, World!"  # 待发送的数据报

# 创建UDP Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 发送数据报到服务端
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

# 关闭Socket
sock.close()
