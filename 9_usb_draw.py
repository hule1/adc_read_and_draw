import queue
import threading
import csv
import time
import ctypes

import numpy as np
import matplotlib.pyplot as plt

import pyqtgraph as pg
import array

pg.setConfigOption('background', 'w')

# 加载DLL
dll = ctypes.WinDLL("easyusb_card_dll.dll")


class SaveThread(threading.Thread):
    def __init__(self, data_queue, plot_queue):
        threading.Thread.__init__(self)
        self.data_queue = data_queue
        self.plot_queue = plot_queue
        self.file = None
        self.lock = threading.Lock()

    def run(self):
        while True:
            if not self.data_queue.empty():
                with self.lock:
                    data = self.data_queue.get()
                    # self.plot_queue.put(data)

                    if self.file is None:
                        # 如果文件还未创建，则打开文件并写入表头
                        self.file = open('data.csv', 'w', newline='')
                        writer = csv.writer(self.file)
                    # 将数据写入文件
                    writer.writerow(data)
            else:
                time.sleep(0.01)


class CollectThread(threading.Thread):
    def __init__(self, data_queue,plot_queue):
        threading.Thread.__init__(self)
        self.data_queue = data_queue
        self.plot_queue = plot_queue
        self.databuf = (ctypes.c_float * 1024)()
        self.ret = None

    def run(self):
        dll.OpenUsbV20()
        while True:
            dll.ADContinuV20(0, 1024, 10000, self.databuf)
            self.ret = 0
            data = list(self.databuf)
            self.data_queue.put(data)
            self.plot_queue.put(data)

    def get_data(self):
        return list(self.databuf)


class PlotThread(threading.Thread):
    def __init__(self, plot_queue):
        threading.Thread.__init__(self)
        self.plot_queue = plot_queue

    def run(self):
        pass
        while True:
            if not self.plot_queue.empty():
                plot_data = self.plot_queue.get()
                curve.setData(plot_data)


if __name__ == '__main__':
    app = pg.mkQApp()  # 建立app
    win = pg.GraphicsWindow()  # 建立窗口
    win.setWindowTitle(u'pyqtgraph逐点画波形图')
    win.resize(800, 500)  # 小窗口大小
    data = array.array('i')  # 可动态改变数组的大小,double型数组
    historyLength = 1024  # 横坐标长度
    a = 0
    data = np.zeros(historyLength).__array__('d')  # 把数组长度设为historyLength、类型为float32

    p = win.addPlot()  # 把图p加入到窗口中

    p.showGrid(x=True, y=True)  # 把X和Y的表格打开
    p.setRange(xRange=[0, historyLength], yRange=[0, 5], padding=0)
    p.setLabel(axis='left', text='y / V')  # 靠左
    p.setLabel(axis='bottom', text='x / point')
    p.setTitle('semg')  # 表格的名字

    curve = p.plot(pen=pg.mkPen(width=5, color='r'))  # 绘制一个图形
    curve.setData(data)

    data_queue = queue.Queue()
    plot_queue = queue.Queue()

    save_thread = SaveThread(data_queue, plot_queue)
    collect_thread = CollectThread(data_queue, plot_queue)
    plot_thread = PlotThread(plot_queue)

    save_thread.start()
    collect_thread.start()
    plot_thread.start()
    # timer = pg.QtCore.QTimer()
    # timer.timeout.connect(plotData)  # 定时刷新数据显示
    # timer.start(1)  # 多少ms调用一次
    app.exec_()
