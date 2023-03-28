# -*- coding: utf-8 -*-
# @Author  : liuqi
# @Time    : 2023/3/24 22:25
# @Function:
# import numpy as np
# import matplotlib.pyplot as plt
# cimport numpy as np
# cdef extern from "your_c_library.h":
#     int DADataSendV20(int chan, int Num, int *databuf)
#
# def generate_sine_wave(freq, duration, amplitude, sample_rate):
#     # Calculate the number of samples needed
#     num_samples = int(sample_rate * duration)
#     # Generate a time array
#     time_array = np.linspace(0, duration, num_samples)
#     # Generate a sine wave using numpy
#     sine_wave = amplitude * np.sin(2 * np.pi * freq * time_array)
#     return sine_wave.astype(np.int32)
#
# def send_sine_wave(freq, duration, amplitude, sample_rate):
#     # Generate the sine wave
#     sine_wave = generate_sine_wave(freq, duration, amplitude, sample_rate)
#     # Convert the numpy array to a C array
#     cdef int *data = &sine_wave[0]
#     # Call the C function with the C array
#     DADataSendV20(0, len(sine_wave), data)
#
#     # Plot the sine wave
#     plt.plot(sine_wave)
#     plt.show()
#
# # Example usage
# send_sine_wave(freq=440, duration=1, amplitude=1000, sample_rate=44100)
