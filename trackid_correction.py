import numpy as np
from math import sqrt
from data_gathering import get_data

file_no = 3

data_now = get_data(file_no)

grid = np.zeros((13, 15))
grid = np.full_like(grid, -1)

pos = []

for snapshot in range(len(data_now)):
    # order of indices in pos:
    # 1st: snapshot no.
    # 2nd: particle no. (not trakID!!)
    # 3rd: info about the parrticle in this order: trackID, x-pos, y-pos, z-pos
    pos_now = []
    part_in_snap = 0
    for tid, particle in enumerate(data_now[snapshot]):
        if particle[0] != 0 and particle[1] != 0 and particle[2] != 0:
            pos_now.append([tid, particle[0], particle[1], particle[2]])
            part_in_snap += 1
    # if part_in_snap > max_part:
    #     max_part = part_in_snap
    # if len(pos_now) > 0:
    pos.append(pos_now)

# Initialisation (1st frame)

first = pos[0][0]
grid[6][7] = first[0]  # trackID of first particle in snapshot 0

ok = 0 # used to not process the first particle again
for particle in pos[0]:
    if ok == 0:
        ok = 1
        continue

    j = round(-(particle[3] - first[3]) / 35.)
    i = round(sqrt((particle[1] - first[1])**2 + (particle[2] - first[2])**2) / 35.)
    if particle[1] - first[1] + particle[2] - particle[2] < 1:
        i = -i

    if abs(i) > 6:
        i = 6 * np.sign(i)
    if abs(j) > 7:
        j = 7 * np.sign(j)

    grid[6 + i, 7 + j] = particle[0]

# Updating (the rest)

print("I am alive!")
print(grid)


