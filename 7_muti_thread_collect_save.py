# -*- coding: utf-8 -*-
# @Author  : liuqi
# @Time    : 2023/3/27 16:43
# @Function:


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
        # self.data_fifo_flag = True
        data_fifo_flag = True


def save_thread(self):
    """
        追加csv文件的数据
    :return:
    """
    # Convert the data buffer to a NumPy array for easier processing
    if self.data_fifo_flag:
        print(1)
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
