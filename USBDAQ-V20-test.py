from ctypes import *

V = 2.0
value = int(V * 4095 / 3.3)

# stdcall调用约定：两种加载方式
# DAQdll = ctypes.windll.LoadLibrary("dllpath")
DAQdll = WinDLL("easyusb_card_dll.dll")
# cdecl调用约定：两种加载方式
# DAQdll = ctypes.cdll.LoadLibrary("dllpath")
# DAQdll = ctypes.CDLL("dllpath")
# <span style="font-family:Microsoft YaHei;">

# 首先打开设备
erro = DAQdll.OpenUsbV20()

# 由于int __stdcall ADSingleV20(int chan,float* adResult);
# 函数需要返回一个采集结果，使用float*传入一个地址，采集结果写入这个指针所指向的地址，
# 所以需要先申明一个float类型的变量，然后使用byref得到这个变量地址当做指针传给函数
advalue = c_float(1)  #
DAQdll.DASingleOutV20(1, value)
# 调用函数采集通道1的电压，单端模式，量程默认正负10V
erro = DAQdll.ADSingleV20(0, byref(advalue))
# 打印采集到的电压值
print(advalue.value)
# 最后需要关闭设备
erro = DAQdll.CloseUsbV20()
