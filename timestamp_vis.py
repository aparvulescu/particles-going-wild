from data_gathering import get_data
import mpl_toolkits.mplot3d as p3
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

file_no = 0

fig = plt.figure()
ax = p3.Axes3D(fig)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# ax.set_title("Hope this finally fucking works", loc='center')
fig.suptitle(f"3D position of markers of Case{file_no}.dat", fontsize=16)

pos = []
snapshot = 0


data_now = get_data(file_no)

for snapshot in range(len(data_now)):
    pos_now = []
    for particle in data_now[snapshot]:
        if particle[0] != 0 and particle[1] != 0 and particle[2] != 0:
            pos_now.append([particle[0], particle[1], particle[2]])
    pos.append(pos_now)

scatters = [ax.scatter(pos[0][i][0:1], pos[0][i][1:2], pos[0][i][2:]) for i in range(len(pos[0]))]

iterations = len(pos)


def animate_scatters(iteration, pos, scatters):
    """
    Update the data held by the scatter plot and therefore animates it.
    Args:
        iteration (int): Current iteration of the animation
        data (list): List of the data positions at each iteration.
        scatters (list): List of all the scatters (One per element)
    Returns:
        list: List of scatters (One per element) with new coordinates
    """
    for i in range(len(pos[0])):
        scatters[i]._offsets3d = (pos[iteration][i][0:1], pos[iteration][i][1:2], pos[iteration][i][2:])
    fig.suptitle(f"3D marker pos at snapshot {iteration} of Case{file_no}.dat", fontsize=16)
    return scatters



# ax.view_init(25, 10)

ani = animation.FuncAnimation(fig, animate_scatters, iterations, fargs=(pos, scatters), interval=10, repeat=True)

plt.show()
