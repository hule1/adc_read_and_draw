import queue
import threading
import csv
import time
import ctypes

import numpy as np

# 加载DLL
dll = ctypes.WinDLL("easyusb_card_dll.dll")


class SaveThread(threading.Thread):
    def __init__(self, data_queue):
        threading.Thread.__init__(self)
        self.data_queue = data_queue
        self.file = None
        self.lock = threading.Lock()

    def run(self):
        while True:
            if not self.data_queue.empty():
                print(self.data_queue.empty())
                with self.lock:
                    data = self.data_queue.get()
                    if self.file is None:
                        # 如果文件还未创建，则打开文件并写入表头
                        self.file = open('data.csv', 'w', newline='')
                        writer = csv.writer(self.file)
                    # 将数据写入文件
                    writer.writerow(data)
            else:
                time.sleep(0.01)


class CollectThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.databuf = (ctypes.c_float * 1024)()
        self.ret = None

    def run(self):
        dll.OpenUsbV20()
        while True:
            dll.ADContinuV20(0, 1024, 10000, self.databuf)
            self.ret = 0

    def get_data(self):
        return list(self.databuf)


if __name__ == '__main__':
    data_queue = queue.Queue()

    save_thread = SaveThread(data_queue)

    collect_thread = CollectThread()

    save_thread.start()
    collect_thread.start()

    while True:
        if collect_thread.ret == 0:
            data = collect_thread.get_data()
            data_queue.put(data)
            collect_thread.ret = 1
