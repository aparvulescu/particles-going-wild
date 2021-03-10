import numpy as np

# Algorithm for the visualisation of the 3D positions of the paticles in time

def get_data(file_no):

    f = open("data\Case" + str(file_no) + ".dat", 'r')

    data = np.zeros((5001, 20001, 11))  # (snapshot, trackID, values)
    times = np.array([]) 
    snapshot = -1
    no_part = 0
    time = -1
    i = 0

    for line in f.readlines():
        if line.startswith("TITLE") or line.startswith("VARIABLES") or line.startswith("DATAPACKING") or line.startswith("I="):
            continue
        if line.startswith("ZONE"):
            snapshot = int(line.split(' ')[2][:-2])
            # print(f"Snapshot = {snapshot}")
            continue
        if line.startswith("STRANDID"):
            time = float(line.split('=')[2])
            times = np.append(times, time)
            # print(f"Time = {time}")
            continue
        values = line.split(' ')
        tid = int(values[8]) # trackID
        data[snapshot][tid][0] = values[0]  # x-position
        data[snapshot][tid][1] = values[1]  # y-position
        data[snapshot][tid][2] = values[2]  # z-position
        data[snapshot][tid][3] = values[4]  # x-velocity (u)
        data[snapshot][tid][4] = values[5]  # y-velocity (v)
        data[snapshot][tid][5] = values[6]  # z-velocity (w)
        data[snapshot][tid][6] = values[7]  # Speed magnitude (|V|)
        data[snapshot][tid][7] = values[9]  # x-acceleration (ax)
        data[snapshot][tid][8] = values[10] # y-acceleration (ay)
        data[snapshot][tid][9] = values[11] # z-acceleration (az)
        data[snapshot][tid][10] = values[12] # acceleration magnitude (|a|)
    f.close()

    return data


# file_no = input("Select .dat file to import [integer between 0 and 2]: ")

# print(times)

# print(data[1540][6145])

# data_now = get_data(1)

# print(data_now[2][2])
