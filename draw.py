# -*- coding: utf-8 -*-
# @Author  : liuqi
# @Time    : 2023/3/24 13:46
# @Function:
import socket
import struct

class Draw:

    def __init__(self):
        self.ip_port = ('127.0.0.1', 40001)
        self.server = None
        self.BUFSIZE = 5000

    def udp_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp协议
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024 * 1024)  # 设置套接字缓冲区大小为1MB
        self.server.bind(self.ip_port)
        while True:
            data2, client_addr = self.server.recvfrom(self.BUFSIZE)

            # 解析二进制数据
            array = struct.unpack('!{}f'.format(len(data2) // 4), data2)

            # 打印接收到的浮点数数组
            print(array)



    def main(self):
        self.udp_server()


if __name__ == '__main__':
   draw = Draw()
   draw.main()