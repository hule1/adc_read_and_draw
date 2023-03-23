# -*- coding: utf-8 -*-
# @Author  : liuqi
# @Time    : 2023/3/23 20:04
# @Function:

from ctypes import *
import numpy as np

import csv


class ADC_read_and_save:
    """

    """
    def __init__(self):
        # 调用动态链接库
        self.DAQdll = WinDLL("easyusb_card_dll.dll")

        # set 输出数据
        V = 2.0
        self.value = int(V * 4095 / 3.3)

        # Define the channel number, number of samples, frequency, and data buffer
        self.chan = 0
        self.num_samples = 1024
        self.frequency = 10000
        self.databuf = (c_float * self.num_samples)()

    def main(self):
        self.open_device()
        self.output_data()
        self.read_data()
        self.save_data()

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
        r = self.DAQdll.DASingleOutV20(1, self.value)

    def read_data(self):
        """
            读取数据
        :return:
        """
        result = self.DAQdll.ADContinuV20(self.chan, self.num_samples, self.frequency, self.databuf)
        # Check if the function call was successful
        if result != 0:
            print('Error: ADContinuV20 returned', result)
        else:
            # Convert the data buffer to a NumPy array for easier processing
            data = np.array(self.databuf)
            print('Data:', data)

    def save_data(self):
        """
            追加csv文件的数据
        :return:
        """
        with open('data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.databuf)

        file.close()


if __name__ == '__main__':
    adc_draw = ADC_read_and_save()
    adc_draw.main()
