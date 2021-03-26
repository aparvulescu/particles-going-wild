from data_gathering import get_data
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
file_no = 0
data_now = get_data(file_no)
pos = []
snapshot = 0
max_part = 0

#help how do i make this a .py? 

for snapshot in range(len(data_now)):
    pos_now = []
    part_in_snap = 0
    for particle in data_now[snapshot]:
        if particle[0] != 0 and particle[1] != 0:  # and particle[2] != 0:
            pos_now.append([particle[0], particle[1]])
            part_in_snap += 1
    if part_in_snap > max_part:
        max_part = part_in_snap
    if len(pos_now) > 0:
        pos.append(pos_now)

for snapshot in pos:
    while len(snapshot) < max_part:
        snapshot.append(snapshot[0])

iterations = len(pos)

snapshot_lst = []
x_pos_lst=[]
y_pos_lst= []
for i in range(iterations):
    part = []
    x_pos =[]
    y_pos= []
    for j in range(len(pos[i])):
        part.append(i)
        x_pos.append(pos[i][j][0])
        y_pos.append(pos[i][j][1])
    snapshot_lst.append(part)
    x_pos_lst.append(x_pos)
    y_pos_lst.append(y_pos)

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

for i in range(len(pos[i])):
    ax1.scatter(snapshot_lst[i], x_pos_lst[i])
    ax2.scatter(snapshot_lst[i],y_pos_lst[i])
fig.suptitle("X and y positions of particles in each iterations")
ax1.title.set_text('x-position over time')
ax2.title.set_text('y-position over time')
ax1.set_ylabel('x-position [mm]')
ax2.set_ylabel('y-position [mm]')

plt.tight_layout()
fig.subplots_adjust(top=0.88)
plt.show()
