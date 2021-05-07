import numpy as np
import matplotlib.pyplot as plt
import math

file_aoa = open("data\\aoa_graph_case1.dat", 'r')

for line in file_aoa.readlines():
    aoa_lst = np.array(list(map(float, line[:-1].split(' '))))

aoa_avg = np.average(aoa_lst)

x = np.arange(0, 3626*0.01,0.01)
y = np.sin(2*0.392*math.pi*x)*(-4) + aoa_avg
print(aoa_avg)

plt.plot(x, aoa_lst)
plt.title('Deflection angle vs time for case 1')
plt.xlabel('Time [s]')
plt.ylabel('Deflection angle [degrees]')
plt.grid(True, which='both')
plt.plot(x, y)
plt.show()
