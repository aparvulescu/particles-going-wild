import numpy as np
from data_gathering.py import get_data

#which file do you want to consider?
file_no = 0
max_snapshot = [100, 3626, 3626]

g = open("data\TrackIDupdate" + str(file_no) + ".dat", 'r')

marker_groups = []
for line in g.readlines():
    curr_marker = list(map(int, line[:-2].split(' ')))
    marker_groups.append(curr_marker)

g.close()
# print(marker_groups)

data = get_data(file_no)
x_avg = []

for marker in marker_groups:
    x_sum = 0
    no_x = 0
    for snapshot in range(max_snapshot[file_no]):
        for tid in marker:
            x_pos = data[snapshot][tid][0]
            if x_pos < 0:
                x_sum += x_pos
                no_x += 1
    if no_x > 10:
        x_avg.append(x_sum / no_x)
    
if len(marker_groups) != len(x_avg):
    print(f"Ha! We found {len(marker_groups) - len(x_avg)} outliers and removed them. You're welcome.\n")

#print(x_avg)

groups = np.full_like(np.zeros(len(x_avg)), -1)
#print(groups)

r = 10  # [mm]

markers_left = x_avg.copy()
curr_group_no = 0
origin_x = markers_left[0]

while len(markers_left) > 0:
    i = 1
    while i < len(markers_left):
        target_x = markers_left[i]
        distance = abs(target_x - origin_x)
        if distance < r:
            index = x_avg.index(target_x)
            groups[index] = curr_group_no
            markers_left.remove(target_x)
        else:
            i += 1
    index = x_avg.index(origin_x)
    groups[index] = curr_group_no
    markers_left.remove(origin_x)
    curr_group_no += 1
    if len(markers_left) > 0:
        origin_x = markers_left[0]

print(groups)

x_new_avg = np.zeros(int(max(groups)) + 1)
no_new_avg = np.zeros(int(max(groups)) + 1)

for index_mk, marker_group in enumerate(groups):
    x_new_avg[int(marker_group)] += x_avg[index_mk]
    no_new_avg[int(marker_group)] += 1

x_new_avg = x_new_avg / no_new_avg

sorted_x_new_avg = np.sort(x_new_avg)

length_sorted = len(sorted_x_new_avg)

body = []
flap = []

for i in range(int(length_sorted * 5 / 8)):
    body.append(np.squeeze(np.where(x_new_avg == sorted_x_new_avg[i])))

for i in range(int(length_sorted * 5 / 8), int(length_sorted)):
    flap.append(np.squeeze(np.where(x_new_avg == sorted_x_new_avg[i])))

print(body)
print(flap)


