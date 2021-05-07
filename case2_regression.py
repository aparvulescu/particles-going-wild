import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from math import *

# Algorithm for the visualisation of the 3D positions of the paticles in time
max_snapshot = [100, 3626, 3626]
#file_no = 0  # input("Select .dat file to import [integer between 0 and 2]: ")

print("Gathering data. Please wait...")

flap_file = open("data\\FlapTID_2.dat", 'r')

flap_tid2 = []
for line in flap_file.readlines():
    flap_tid2 = list(map(int, line[:-1].split(' ')))

flap_file.close()

flap_file = open("data\\FlapTID_1.dat", 'r')

flap_tid1 = []
for line in flap_file.readlines():
    flap_tid1 = list(map(int, line[:-1].split(' ')))

flap_file.close()

# print(flap_tid2)

f = open("data\\Case" + str(2) + ".dat", 'r')

data = np.zeros((5001, 20001, 2))  # (snapshot, trackID, values)
times = np.array([])
snapshot = -1
no_part = 0
time = -1

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
    if tid not in flap_tid2:
        continue
    #    print(tid)
    data[snapshot][tid][0] = values[0]  # x-position
    data[snapshot][tid][1] = values[1]  # y-position
    #data[snapshot][tid][2] = values[2]  # z-position
    # data[snapshot][tid][3] = values[4]  # x-velocity (u)
    # data[snapshot][tid][4] = values[5]  # y-velocity (v)
    # data[snapshot][tid][5] = values[6]  # z-velocity (w)
    # data[snapshot][tid][6] = values[7]  # Speed magnitude (|V|)
    # data[snapshot][tid][7] = values[9]  # x-acceleration (ax)
    # data[snapshot][tid][8] = values[10]  # y-acceleration (ay)
    # data[snapshot][tid][9] = values[11]  # z-acceleration (az)
    # data[snapshot][tid][10] = values[12]  # acceleration magnitude (|a|)

f.close()

f1 = open("data\\Case1.dat", 'r')

data1 = np.zeros((3627, 20001, 2))  # (snapshot, trackID, values)
times1 = np.array([])
snapshot1 = -1
no_part1 = 0
time1 = -1

for line1 in f1.readlines():
    if line1.startswith("TITLE") or line1.startswith("VARIABLES") or line1.startswith(
            "DATAPACKING") or line1.startswith(
            "I="):
        continue
    if line1.startswith("ZONE"):
        snapshot1 = int(line1.split(' ')[2][:-2])
        # print(f"Snapshot = {snapshot}")
        continue
    if line1.startswith("STRANDID"):
        time1 = float(line1.split('=')[2])
        times1 = np.append(times1, time1)
        # print(f"Time = {time}")
        continue
    values1 = line1.split(' ')
    tid1 = int(values1[8])  # trackID
    if tid1 not in flap_tid1:
        continue
    #    print(tid)
    data1[snapshot1][tid1][0] = values1[0]  # x-position
    data1[snapshot1][tid1][1] = values1[1]  # y-position
    #data0[snapshot0][tid0][2] = values0[2]  # z-position
    # data0[snapshot][tid][3] = values[4]  # x-velocity (u)
    # data0[snapshot][tid][4] = values[5]  # y-velocity (v)
    # data0[snapshot][tid][5] = values[6]  # z-velocity (w)
    # data0[snapshot][tid][6] = values[7]  # Speed magnitude (|V|)
    # data0[snapshot][tid][7] = values[9]  # x-acceleration (ax)
    # data0[snapshot][tid][8] = values[10]  # y-acceleration (ay)
    # data0[snapshot][tid][9] = values[11]  # z-acceleration (az)
    # data0[snapshot][tid][10] = values[12]  # acceleration magnitude (|a|)

g = open("data\\TrackIDupdate" + str(1) + ".dat", 'r')

marker_groups = []
for line in g.readlines():
    curr_marker = list(map(int, line[:-2].split(' ')))
    marker_groups.append(curr_marker)

# g.close()
# # print(marker_groups)

# x_avg = []

# for marker in marker_groups:
#     no_x = 0
#     for snapshot in range(max_snapshot[1]):
#         for tid in marker:
#             x_pos = data1[snapshot][tid][0]
#             y_pos = data1[snapshot][tid][1]
#             if x_pos < 0:
#                 no_x += 1
#     if no_x < 20:
#         for snapshot in range(max_snapshot[1]):
#             for tid in marker:
#                 data1[snapshot][tid] = 0
#                 # data[snapshot][tid] = 0
#                 # data[snapshot][tid]

f.close()

f1.close()

print("Finished gathering data! Now starting linear algebra.")



parameter = max_snapshot[2]   #parameter = 500 #int(input('Which snapshot do you want to observe '))

delta_lst = []

for p in range(parameter):
    # here starts case 2
    i = 0
    x_value_lst = []
    y_value_lst = []
    time_lst = []

    while i < 20001:
        if data[p][i][0] < int(-1):
            x_value_lst.append(data[p][i][0])
            y_value_lst.append(data[p][i][1])
            
            #z_value_lst.append(data[p][i][2])
            i += 1
        else:
            i += 1
        
        
    number_of_outliers = 1
    while number_of_outliers > 0:
        A_mat = np.zeros((int(len(x_value_lst)), 2))
        y_mat = np.zeros(int(len(x_value_lst)))
        Qy = np.eye(int(len(x_value_lst)))

        for j in range(len(x_value_lst)):
            A_mat[j][0] = 1
            A_mat[j][1] = x_value_lst[j]
            #A_mat[j][2] = y_value_lst[j]
            y_mat[j] = y_value_lst[j]

        A_mat_T = A_mat.transpose()
        ATA = A_mat_T.dot(A_mat)
        ATy = A_mat_T.dot(y_mat)
        ATA_inv = np.linalg.inv(ATA)

        Qy_inv = np.linalg.inv(Qy)
        Qx = np.linalg.inv(A_mat_T.dot(Qy_inv.dot(A_mat)))
        Qe = Qy - A_mat.dot(Qx.dot(A_mat_T))

        sigma_e = np.zeros(Qe.shape[0])
        for i in range(Qe.shape[0]):
            sigma_e[i] = np.sqrt(Qe[i, i])

        a = ATA_inv.dot(ATy)

        e_vec = y_mat - A_mat.dot(a)
        e_norm = np.zeros(len(e_vec))

        for i in range(len(e_vec)):
            e_norm[i] = abs(e_vec[i] / sigma_e[i])

        number_of_outliers = 0
        outliers_lst = []
        for i in range(len(e_norm)):
            if e_norm[i] > 2:
                number_of_outliers += 1
                outliers_lst.append(i)
        
        x_value_lst = np.delete(x_value_lst, outliers_lst)
        y_value_lst = np.delete(y_value_lst, outliers_lst)
    
    a2 = a.copy()
    # Here starts the end of everything (case 1)

    i = 0
    x_value_lst = []
    y_value_lst = []
    time_lst = []

    while i < 20001:
        if data1[p][i][0] < int(-1):
            x_value_lst.append(data1[p][i][0])
            y_value_lst.append(data1[p][i][1])
            
            #z_value_lst.append(data[p][i][2])
            i += 1
        else:
            i += 1
        
        
    number_of_outliers = 1
    while number_of_outliers > 0:
        A_mat = np.zeros((int(len(x_value_lst)), 2))
        y_mat = np.zeros(int(len(x_value_lst)))
        Qy = np.eye(int(len(x_value_lst)))

        for j in range(len(x_value_lst)):
            A_mat[j][0] = 1
            A_mat[j][1] = x_value_lst[j]
            #A_mat[j][2] = y_value_lst[j]
            y_mat[j] = y_value_lst[j]

        A_mat_T = A_mat.transpose()
        ATA = A_mat_T.dot(A_mat)
        ATy = A_mat_T.dot(y_mat)
        ATA_inv = np.linalg.inv(ATA)

        Qy_inv = np.linalg.inv(Qy)
        Qx = np.linalg.inv(A_mat_T.dot(Qy_inv.dot(A_mat)))
        Qe = Qy - A_mat.dot(Qx.dot(A_mat_T))

        sigma_e = np.zeros(Qe.shape[0])
        for i in range(Qe.shape[0]):
            sigma_e[i] = np.sqrt(Qe[i, i])

        a = ATA_inv.dot(ATy)

        e_vec = y_mat - A_mat.dot(a)
        e_norm = np.zeros(len(e_vec))

        for i in range(len(e_vec)):
            e_norm[i] = abs(e_vec[i] / sigma_e[i])

        number_of_outliers = 0
        outliers_lst = []
        for i in range(len(e_norm)):
            if e_norm[i] > 2:
                number_of_outliers += 1
                outliers_lst.append(i)
        
        x_value_lst = np.delete(x_value_lst, outliers_lst)
        y_value_lst = np.delete(y_value_lst, outliers_lst)

    a1 = a.copy()

    print(f"Just finished snapshot {p}!")

    delta = atan2(a2[1]-a1[1], 1+a2[1]*a1[1])
    delta_lst.append(degrees(delta))

delta_file = open("data\\delta_graph_case2.dat", 'w')
for i in range(len(delta_lst)):
    delta_file.write(f"{delta_lst[i]} ")

delta_file.close()

x = np.arange(0,parameter*0.01,0.01)
y = np.sin(2*0.39*pi*x)*(-4)

plt.plot(x, delta_lst)
#plt.title('Angle of attack vs time for case 1')
plt.xlabel('Time [s]')
plt.ylabel('Angle of attack [degrees]')
plt.grid(True, which='both')
plt.plot(x, y)
plt.show()
