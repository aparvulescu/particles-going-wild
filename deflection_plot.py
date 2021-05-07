import numpy as np
import matplotlib.pyplot as plt
import math

file_delta = open("data\\delta_graph_case2.dat", 'r')

for line in file_delta.readlines():
    delta_lst = np.array(list(map(float, line[:-1].split(' '))))

delta_avg = np.average(delta_lst)

x = np.arange(0, 3626*0.01,0.01)
y = np.sin(2*0.392*math.pi*x)*(8.1) + delta_avg
print(delta_avg)

plt.plot(x, delta_lst)
plt.title('Deflection angle vs time for case 2')
plt.xlabel('Time [s]')
plt.ylabel('Deflection angle [degrees]')
plt.grid(True, which='both')
plt.plot(x, y)
plt.show()
