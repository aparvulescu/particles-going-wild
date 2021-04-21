import numpy as np
#import re


# Algorithm for the visualisation of the 3D positions of the paticles in time

def get_data(file_no):
    global values, tid, track_id_per_snapshot
    f = open("data\Case" + str(file_no) + ".dat", 'r')

    data = np.zeros((5001, 20001, 11))  # (snapshot, trackID, values)
    times = np.array([])
    max_snapshot = [100, 3626, 3626]
    track_id_per_snapshot = np.zeros((max_snapshot[file_no], 70))
    track_id_per_snapshot = np.full_like(track_id_per_snapshot, -1)
    #track_id_per_snapshot_00 = np.zeros(max_snapshot[file_no])
    snapshot = -1
    no_part = 0
    time = -1
    i = 0

    for line in f.readlines():
        if line.startswith("TITLE") or line.startswith("VARIABLES") or line.startswith(
                "DATAPACKING"):
            i = 0
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
        if line.startswith("I"):
            intermediate = str(line.split('=')[1])
            I = int(intermediate[0:2])
            continue
        values = line.split(' ')
        tid = int(values[8])  # trackID
        data[snapshot][tid][0] = values[0]  # x-position
        data[snapshot][tid][1] = values[1]  # y-position
        data[snapshot][tid][2] = values[2]  # z-positionx
        data[snapshot][tid][3] = values[4]  # x-velocity (u)
        data[snapshot][tid][4] = values[5]  # y-velocity (v)
        data[snapshot][tid][5] = values[6]  # z-velocity (w)
        data[snapshot][tid][6] = values[7]  # Speed magnitude (|V|)
        data[snapshot][tid][7] = values[9]  # x-acceleration (ax)
        data[snapshot][tid][8] = values[10]  # y-acceleration (ay)
        data[snapshot][tid][9] = values[11]  # z-acceleration (az)
        data[snapshot][tid][10] = values[12]  # acceleration magnitude (|a|)

        track_id_per_snapshot[snapshot][i] = tid
        i += 1
    f.close()
    #for n in range(max_snapshot[file_no]):
        #track_id_per_snapshot = np.trim_zeros([track_id_per_snapshot_00[n]], 'b')
        #track_id_per_snapshot[n] = np.append(track_id_per_snapshot_zeros)
    #p = np.where(track_id_per_snapshot_00 != 0)
    #track_id_per_snapshot_00 = track_id_per_snapshot_00[min(p[1]): max(p[1]) + 1]
    return data, values, track_id_per_snapshot


# file_no = input("Select .dat file to import [integer between 0 and 2]: ")
#track_id_per_snapshot = get_data(0)[2]




# print(times)
