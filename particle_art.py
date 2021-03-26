import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import interpolate, integrate

# Algorithm for the visualisation of the 3D positions of the paticles in time

# file_no = input("Select .dat file to import [integer between 0 and 2]: ")
file_no = 2

f = open("data\Case" + str(file_no) + ".dat", 'r')

data = np.zeros((5001, 20001, 16))  # (snapshot, trackID, values)
times = np.array([])
snapshot = -1
no_part = 0
time = -1
#hello

for line in f.readlines():
    if line.startswith("TITLE") or line.startswith("VARIABLES") or line.startswith("DATAPACKING") or line.startswith(
            "I="):
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
    tid = int(values[8])  # trackID
#    print(tid)
    data[snapshot][tid][0] = values[0]  # x-position
    data[snapshot][tid][1] = values[1]  # y-position
    data[snapshot][tid][2] = values[2]  # z-position
    data[snapshot][tid][3] = values[4]  # x-velocity (u)
    data[snapshot][tid][4] = values[5]  # y-velocity (v)
    data[snapshot][tid][5] = values[6]  # z-velocity (w)
    data[snapshot][tid][6] = values[7]  # Speed magnitude (|V|)
    data[snapshot][tid][7] = values[9]  # x-acceleration (ax)
    data[snapshot][tid][8] = values[10]  # y-acceleration (ay)
    data[snapshot][tid][9] = values[11]  # z-acceleration (az)
    data[snapshot][tid][10] = values[12]  # acceleration magnitude (|a|)
    data[snapshot][tid][11] = values[8]     #

f.close()


track_id_file = open(f"data\TrackIDUpdate{file_no}.dat", 'r')

marker_tid_list = []

for line in track_id_file.readlines():
    marker_tid_list.append([])
    numbers = line.split(' ')
    numbers.remove('\n')
    for number in numbers:
        marker_tid_list[-1].append(int(number))
        
print(marker_tid_list[0])

# parameter = input('Which parameter do you want to observe? (e.g.: x, y, u,v )')
parameter = 'x'
# track = int(input('Which particle do you want to track?'))
marker_index = 42
tracks = marker_tid_list[marker_index]
para_lst = [ 'x' ,'y','z','u','v','w', 'V','ax','ay','az','a']
parameter = para_lst.index(str(parameter))
#sad



y_value_lst = []
time_lst = []

print(tracks)

for track in tracks:
    i = 0
    while i < 5001:
        if data[i][track][0] < int(-1):
            y_value_lst.append(data[i][track][parameter])
            time_lst.append(times[i])
            i += 1
        else:
            i += 1


plt.plot(time_lst, y_value_lst , 'o-')
plt.xlabel('time [s]')
plt.ylabel(para_lst[parameter])

plt.show()