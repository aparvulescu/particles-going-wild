

from data_gathering import get_data
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

x = np.array([])
y = np.array([])
z = np.array([])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ln, = ax.scatter(x[0], y[0], z[0], 'o')


pos = []
snapshot = 0
file_no = 1


data_now = get_data(1)

for snapshot in range(len(data_now)):
    pos_now = []
    for particle in data_now[snapshot]:
        if particle[0] != 0 and particle[1] != 0 and particle[2] != 0:
            pos_now.append([particle[0], particle[1], particle[2]])
            #x = np.append(x, particle[0])
            #y = np.append(y, particle[1])
            #z = np.append(z, particle[2])
    pos.append(pos_now)

def update(frame):
    x = np.append(x, frame)
    y = np.append(y, np.sin(frame))
    z = np.append(z, np.cos(frame))






ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

ani = animation.FuncAnimation(fig, update, 100)

plt.show()




