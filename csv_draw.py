import matplotlib.pyplot as plt
import csv
import numpy as np

start_index = 0
end_index = 1023

arr_y = []

with open('data.csv', 'r') as csvfile:
    plots = csv.reader(csvfile)
    for row in plots:
        arr_y.append(list(map(float, row)))

x = range(1, len(arr_y[0]) + 1)

arr_y = np.array(arr_y)
flat_arr_y = arr_y.flatten()
#
# for i in range(arr_y.shape(0)):
#     z = np.concatenate([arr_y[0], arr_y[1]])
# z = y[0] + y[1]
# for i in range(2):
#     plt.plot(x, y[i])

plt.plot(flat_arr_y[1000:7000])

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('CSV Data')
plt.show()
