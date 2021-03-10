from data_gathering import get_data
import matplotlib.pyplot as plt
import numpy as np

snapshot = 0
file_no = 1
x = np.array([])
y = np.array([])
z = np.array([])

data_now = get_data(1)

for particle in data_now[snapshot]:
    x = np.append(x, particle[0])
    y = np.append(y, particle[1])
    z = np.append(z, particle[2])

plt.plot(x, y, z)
plt.show()


