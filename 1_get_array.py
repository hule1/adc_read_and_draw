from ctypes import *
import numpy as np

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
if erro != 0:
    print('Error: OpenUsbV20 returned', erro)
# Define the argument types and return type for the function
#DAQdll.ADContinuV20.argtypes = [c_int, c_int, c_int, POINTER(c_float)]
#DAQdll.ADContinuV20.restype = c_int

#set ad1 out 1
r=DAQdll.DASingleOutV20(1, value)

# Define the channel number, number of samples, frequency, and data buffer
chan = 0
num_samples = 1024
frequency = 10000
databuf = (c_float * num_samples)()

# Call the function
result = DAQdll.ADContinuV20(chan, num_samples, frequency, databuf)


# Check if the function call was successful
if result != 0:
    print('Error: ADContinuV20 returned', result)
else:
    # Convert the data buffer to a NumPy array for easier processing
    data = np.array(databuf)
    print('Data:', data)