from data_gathering import get_data
import mpl_toolkits.mplot3d as p3
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import matplotlib as mpl
mpl.rcParams['animation.ffmpeg_path'] = r'E:\\Documente Andrei\\Setupuri\\ffmpeg-4.3.2-2021-02-27-essentials_build\\bin\\ffmpeg.exe'

file_no = 2

fig = plt.figure()
ax = p3.Axes3D(fig)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

ax.view_init(elev=90., azim=145.)

# ax.set_title("Hope this finally fucking works", loc='center')
fig.suptitle(f"3D position of markers of Case{file_no}.dat", fontsize=16)

pos = []
snapshot = 0

data_now = get_data(file_no)
max_part = 0

for snapshot in range(len(data_now)):
    pos_now = []
    part_in_snap = 0
    for particle in data_now[snapshot]:
        if particle[0] != 0 and particle[1] != 0 and particle[2] != 0:
            pos_now.append([particle[0], particle[1], particle[2]])
            part_in_snap += 1
    if part_in_snap > max_part:
        max_part = part_in_snap
    if len(pos_now) > 0:
        pos.append(pos_now)

# print(pos)

for snapshot in pos:
    while len(snapshot) < max_part:
        snapshot.append(snapshot[0])

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
        # something = scatters[i]
    # scatters = [ax.scatter(pos[iteration][i][0:1], pos[iteration][i][1:2], pos[iteration][i][2:]) for i in range(len(pos[iteration]))]
    fig.suptitle(f"3D marker pos at snapshot {iteration} of Case{file_no}.dat", fontsize=16)
    return scatters


# ax.view_init(25, 10)

ani = animation.FuncAnimation(fig, animate_scatters, iterations, fargs=(pos, scatters), repeat=True)

Writer = animation.writers['ffmpeg']
writer = Writer(fps=10, metadata=dict(artist='Me'), bitrate=1800, extra_args=['-vcodec', 'libx264'])
ani.save(f'animated_data_{file_no}.mp4', writer=writer)

plt.show()
