import numpy as np
from data_gathering import get_data

grid = np.zeros((13, 15))
grid = np.full_like(grid, -1)

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

# Initialisation (1st frame)

grid[7][8]

# Updating (the rest)


print(grid)


