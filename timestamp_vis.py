

from data_gathering import get_data
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

snapshot = 0
file_no = 1
x = np.array([])
y = np.array([])
z = np.array([])

data_now = get_data(1)

for particle in data_now[snapshot]:
    if particle[0] != 0 and particle[1] != 0 and particle[2] != 0:
        x = np.append(x, particle[0])
        y = np.append(y, particle[1])
        z = np.append(z, particle[2])


# plt.plot(x, y, z)
# plt.show()


fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot3D(x, y, z, 'o')

plt.show()

