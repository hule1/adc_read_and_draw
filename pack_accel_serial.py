# 功能：绘制连续数据的波形
# 方法：调用之前需先启动ConnectWithTerminal.py程序
# 作者：朱航彪
# 时间：2022/03/25

from asyncio import futures
import pyqtgraph as pg
import array
# import serial
import threading
import numpy as np
from queue import Queue
import time
import socket
import struct
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog, QFileDialog

pg.setConfigOption('background', 'w')

idxPlot = 0
state = 0
idx = 0
addr = []
cnt = []
data_raw = []
data_corrupt = False
data_done = False

q = Queue(maxsize=0)
r = Queue(maxsize=0)
s = Queue(maxsize=0)

BUFSIZE = 4096


def Serial():
    """
        利用udp接受串口程序发来的数据
        然后将数据保存在队列里
    :return:
    """
    global q, r, s
    global vol
    global state
    global idx
    global addr
    global cnt1, cnt2
    global data_raw
    global data_corrupt, data_done
    fulldata = ""
    ip_port = ('127.0.0.1', 40001)
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp协议
    server.bind(ip_port)
    while (True):
        data2, client_addr = server.recvfrom(BUFSIZE)
        data2 = struct.unpack('!f', data2)[0]
        print(data2)
        q.put(data2)


def plotData():
    """
        idxPlot为字长标志位
        当idxPlot小于historyLength时:
            data往后面赋值
        当idx大于historyLength时：
            data列表的数据左移一位，末尾记0
            然后最后一位继续读值
    :return:
    """

    global idxPlot

    if q.qsize() == 0:
        return

    if idxPlot < historyLength:
        data[idxPlot] = q.get()
        idxPlot = idxPlot + 1
    else:
        data[:-1] = data[1:]  # 左移一位
        data[idxPlot - 1] = q.get()  # 读取最后一位
    curve.setData(data)


if __name__ == "__main__":
    app = pg.mkQApp()  # 建立app
    win = pg.GraphicsWindow()  # 建立窗口
    win.setWindowTitle(u'pyqtgraph逐点画波形图')
    win.resize(800, 500)  # 小窗口大小
    data = array.array('i')  # 可动态改变数组的大小,double型数组
    historyLength = 1000  # 横坐标长度
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

    th1 = threading.Thread(target=Serial)
    th1.start()
    timer = pg.QtCore.QTimer()
    timer.timeout.connect(plotData)  # 定时刷新数据显示
    timer.start(1)  # 多少ms调用一次
    app.exec_()
