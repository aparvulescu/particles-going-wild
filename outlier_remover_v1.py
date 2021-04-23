import numpy as np
from data_gathering import get_data

#which file do you want to consider?
file_no = 0
max_snapshot = [100, 3626, 3626]



def get_data_without_outliers(file_no):

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
        no_x = 0
        for snapshot in range(max_snapshot[file_no]):
            for tid in marker:
                x_pos = data[snapshot][tid][0]
                y_pos = data[snapshot][tid][1]
                if x_pos < 0:
                    no_x += 1
        if no_x < 10:
            for snapshot in range(max_snapshot[file_no]):
                for tid in marker:
                    data[snapshot][tid] = 0
                    # data[snapshot][tid] = 0
                    # data[snapshot][tid]
    return data

print(get_data_without_outliers(0))

