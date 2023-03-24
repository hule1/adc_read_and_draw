# -*- coding: utf-8 -*-
# @Author  : liuqi
# @Time    : 2023/3/23 20:04
# @Function:
import time
from ctypes import *
import numpy as np
import csv
import socket
import struct

class ADC_read_and_save:
    """

    """

    def __init__(self):
        # 调用动态链接库
        self.DAQdll = WinDLL("easyusb_card_dll.dll")

        # udp协议
        self.ip_port = ('127.0.0.1', 40001)
        self.client = None

        # set 输出数据
        self.V = 2.0
        self.value = int(self.V * 4095 / 3.3)

        # Define the channel number, number of samples, frequency, and data buffer
        self.chan = 0
        self.num_samples = 1024
        self.frequency = 10000
        self.databuf = (c_float * self.num_samples)()
        self.data = None

    def main(self):
        self.udp()
        self.open_device()
        self.output_data()
        while True:
            # 循环 读取、保存、发送数据
            self.read_data()
            self.save_data()
            self.udp_client_send()
            time.sleep(1)
        client.close()

    def udp(self):
        """
            初始化udp
        :return:
        """
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp协议

    #  self.client.bind(self.ip_port)  # 绑定ip和端口

    def udp_client_send(self):
        """
            向self.ip_port发送数据self.databuf
        :return:
        """
        # 将数值数组打包为二进制数据

        packed_data = struct.pack('!{}f'.format(len(self.data.value)), self.data.value)

        self.client.sendto(packed_data, self.ip_port)

    def open_device(self):
        """
            打开设备
        :return:
        """
        erro = self.DAQdll.OpenUsbV20()
        if erro != 0:
            print('Error: OpenUsbV20 returned', erro)
        # Define the argument types and return type for the function
        # DAQdll.ADContinuV20.argtypes = [c_int, c_int, c_int, POINTER(c_float)]
        # DAQdll.ADContinuV20.restype = c_int

    def output_data(self):
        """
            设置输出数据
        :return:
        """
        # set ad1 out 1
        self.DAQdll.DASingleOutV20(1, self.value)

    def read_data(self):
        """
            读取数据
        :return:
        """
        # 读取数据:信道、采样数、采样频率、数据缓冲列表
        result = self.DAQdll.ADContinuV20(self.chan, self.num_samples, self.frequency, self.databuf)

        # Check if the function call was successful
        if result != 0:
            print('Error: ADContinuV20 returned', result)
        else:
            # Convert the data buffer to a NumPy array for easier processing
            self.data = np.array(self.databuf)

    def save_data(self):
        """
            追加csv文件的数据
        :return:
        """
        with open('data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            # Convert the data buffer to a NumPy array for easier processing
            self.data = np.array(self.databuf)
            writer.writerow(self.data)

        file.close()


if __name__ == '__main__':
    adc_draw = ADC_read_and_save()
    adc_draw.main()
