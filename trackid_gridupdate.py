import numpy as np
from data_gathering_update import get_data
from time import clock

#stopwatch
start_time = time.time()

#which file do you want to consider?
file_no = 0
max_snapshot = [100, 3626, 3626]
dt_arr = [0.014, 0.001, 0.001]  # s? to check Case1.dat and Case2.dat
dt = dt_arr[file_no]

#import from get_Data
data = get_data(file_no)[0]
values = get_data(file_no)[1]
track_id_per_snapshot = get_data(file_no)[2]

#empty marker tid list
marker_tid_list = []  # change to list
marker_last_seen_snp = []

#marker_tid_list.append("first tid for new marker")
#marker_tid_list["index of marker"].append("new_tid")

#choose radius (mm)
r = 10

#open file to write in
track_id_file = open("TrackIDupdate.dat")

for trackid in track_id_per_snapshot[0]:
    if trackid == -1:
        continue
    marker_tid_list.append(trackid)
    marker_last_seen_snp.append(0)


for snapshot in range(1, max_snapshot[file_no]):
    # for marker in marker_tid_list:
        #print("marker", marker_no)
        for n in range(70):  # change to list
            a = int(track_id_per_snapshot[snapshot][n])
            if a == -1:
                continue
            if a in marker_tid_list[:][-1]: 
                marker_last_seen_snp[marker_tid_list[:][-1].index(a)] = snapshot
                continue
            point_coor = np.array([data[snapshot][a][0], data[snapshot][a][1], data[snapshot][a][2]])
            
            ok = False 
            for marker, marker_no in enumerate(marker_tid_list):
                snapshot_old = marker_last_seen_snp[marker_no]
                b = marker[-1]  # last_tid_marker
                time_ago = snapshot - snapshot_old

                origin_coor = np.array([data[snapshot_old][b][0], data[snapshot_old][b][1], data[snapshot_old][b][2]])
                #pythagoras_origin = np.linalg.norm(origin_coor)
                origin_vel = np.array([data[snapshot_old][b][3], data[snapshot_old][b][4], data[snapshot_old][b][5]])
                origin_acc = np.array([data[snapshot_old][b][7], data[snapshot_old][b][8], data[snapshot_old][b][9]])
                #predicted_vel = origin_vel + dt * origin_acc
                predicted_coor = origin_coor + dt * origin_vel + 0.5*dt*dt * origin_acc

                # x = x0 + v0*t + 0.5*a*t^2
                distance = abs(np.linalg.norm(point_coor - predicted_coor))
                if distance < r:
                 #np.append(marker_tid_list[marker_no], b_array)
                    marker_tid_list[marker_no].append(a)
                    marker_last_seen_snp[marker_no] = snapshot
                    ok = True
                    break
            
            if ok == True:
                continue
            else:
                marker_tid_list.append(a)
                marker_last_seen_snp.append(snapshot)


'''
        if snapshot != 0:
            origin_coor = np.array([data[snapshot][b][0], data[snapshot][b][1], data[snapshot][b][2]])
            # pythagoras_origin = np.linalg.norm(origin_coor)
            origin_vel = np.array([data[snapshot][b][3], data[snapshot][b][4], data[snapshot][b][5]])
            origin_acc = np.array([data[snapshot][b][7], data[snapshot][b][8], data[snapshot][b][9]])
            predicted_vel = origin_vel + dt * origin_acc
            predicted_coor = origin_coor + dt * predicted_vel
            for m in range(70):
                c = int(track_id_per_snapshot[snapshot + 1][m])
                point_coor = np.array([data[snapshot + 1][c][0], data[snapshot + 1][c][1], data[snapshot + 1][c][2]])
                distance = np.linalg.norm(point_coor - predicted_coor)
                if distance < r:
                    #np.append(marker_tid_list[marker_no], b_array)
                    marker_tid_list[marker_no].append(c)
'''      

print(marker_tid_list)
print("--- %s seconds ---" % (time.time() - start_time))

# SUMMARY:
# goal; update initial grid with new track-IDs for each snapshot
# for each track-ID in initial snapshot t_0 look for most close neighbour in both x,y,z directions in snapshot t_1
# add some conditions when the found track-ID is not the closest in all three directions
# assign the found track-ID to the grid

# CRITICAL POINTS:
# when a marker is found that wasn't in the grid earlier what to do???
