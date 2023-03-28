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
import threading


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
        self.data_fifo_flag = False
        self.data_fifo = None

    def main(self):
        # # self.udp()
        # self.open_device()
        # # self.output_data()
        # while True:
        #     # 循环 读取、保存、发送数据
        #     self.collect_thread()
        #     self.save_thread()
        #     # self.udp_client_send()
        #     # time.sleep(1)
        self.open_device()
        # 创建线程进行数据采集和数据保存
        collect_t = threading.Thread(target=self.collect_thread)
        collect_t.start()
        save_t = threading.Thread(target=self.save_thread)
        save_t.start()
        # 等待数据保存线程结束
        save_t.join()

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
        packed_data = struct.pack('<{}f'.format(len(self.data)), self.databuf)

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

    def collect_thread(self):
        """
            读取数据
        :return:
        """
        while True:
            # 读取数据:信道、采样数、采样频率、数据缓冲列表
            result = self.DAQdll.ADContinuV20(self.chan, self.num_samples, self.frequency, self.databuf)
            # if databuf_fifo_flag == false
            # databuf_fifo[] = databuf
            # databuf_fifo_flag = true
            # Check if the function call was successful
            if result != 0:
                print('Error: ADContinuV20 returned', result)
            else:
                 self.data_fifo_flag = True


    def save_thread(self):
        """
            追加csv文件的数据
        :return:
        """
        # Convert the data buffer to a NumPy array for easier processing

        if self.data_fifo_flag:
            self.data_fifo = np.array(self.databuf)
            # 保存数据
            with open('data.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                # Convert the data buffer to a NumPy array for easier processing
                # self.data = np.array(self.databuf)
                writer.writerow(self.data)
            self.data_fifo_flag = False
            print(self.data_fifo)
            file.close()


if __name__ == '__main__':
    adc_draw = ADC_read_and_save()
    adc_draw.main()
