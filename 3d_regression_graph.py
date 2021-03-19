import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from math import *
# Algorithm for the visualisation of the 3D positions of the paticles in time

file_no = 1 #input("Select .dat file to import [integer between 0 and 2]: ")

f = open("data\Case" + str(file_no) + ".dat", 'r')

data = np.zeros((5001, 20001, 3))  # (snapshot, trackID, values)
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
#    print(tid)
    data[snapshot][tid][0] = values[0]  # x-position
    data[snapshot][tid][1] = values[1]  # y-position
    data[snapshot][tid][2] = values[2]  # z-position
    # data[snapshot][tid][3] = values[4]  # x-velocity (u)
    # data[snapshot][tid][4] = values[5]  # y-velocity (v)
    # data[snapshot][tid][5] = values[6]  # z-velocity (w)
    # data[snapshot][tid][6] = values[7]  # Speed magnitude (|V|)
    # data[snapshot][tid][7] = values[9]  # x-acceleration (ax)
    # data[snapshot][tid][8] = values[10]  # y-acceleration (ay)
    # data[snapshot][tid][9] = values[11]  # z-acceleration (az)
    # data[snapshot][tid][10] = values[12]  # acceleration magnitude (|a|)


f.close()

f0 = open("data\Case0.dat", 'r')

data0 = np.zeros((101, 20001, 3))  # (snapshot, trackID, values)
times0 = np.array([])
snapshot0 = -1
no_part0 = 0
time0 = -1


for line0 in f0.readlines():
    if line0.startswith("TITLE") or line0.startswith("VARIABLES") or line0.startswith("DATAPACKING") or line0.startswith(
            "I="):
        continue
    if line0.startswith("ZONE"):
        snapshot0 = int(line0.split(' ')[2][:-2])
        # print(f"Snapshot = {snapshot}")
        continue
    if line0.startswith("STRANDID"):
        time0 = float(line0.split('=')[2])
        times0 = np.append(times0, time0)
        # print(f"Time = {time}")
        continue
    values0 = line0.split(' ')
    tid0 = int(values0[8])  # trackID
#    print(tid)
    data0[snapshot0][tid0][0] = values0[0]  # x-position
    data0[snapshot0][tid0][1] = values0[1]  # y-position
    data0[snapshot0][tid0][2] = values0[2]  # z-position
    # data0[snapshot][tid][3] = values[4]  # x-velocity (u)
    # data0[snapshot][tid][4] = values[5]  # y-velocity (v)
    # data0[snapshot][tid][5] = values[6]  # z-velocity (w)
    # data0[snapshot][tid][6] = values[7]  # Speed magnitude (|V|)
    # data0[snapshot][tid][7] = values[9]  # x-acceleration (ax)
    # data0[snapshot][tid][8] = values[10]  # y-acceleration (ay)
    # data0[snapshot][tid][9] = values[11]  # z-acceleration (az)
    # data0[snapshot][tid][10] = values[12]  # acceleration magnitude (|a|)

f0.close()

k = 0
x_value_lst0 = []
y_value_lst0 = []
z_value_lst0 = []
#time_lst0 = []

while k < 20001:
    if data0[0][k][0] < int(-1):
        x_value_lst0.append(data0[0][k][0])
        y_value_lst0.append(data0[0][k][1])
        z_value_lst0.append(data0[0][k][2])
        #time_lst0.append(times0[k])
        k += 1
    else:
        k += 1

A_mat0 = np.zeros((int(len(x_value_lst0)),3))
z_mat0 = np.zeros(int(len(x_value_lst0)))

for l in range(len(x_value_lst0)):
    A_mat0[l][0] = 1
    A_mat0[l][1] = x_value_lst0[l]
    A_mat0[l][2] = y_value_lst0[l]
    z_mat0[l] = z_value_lst0[l]


A_mat_T0 = A_mat0.transpose()
ATA0 = [[sum(a*b for a,b in zip(A_mat_T0_row,A_mat0_col)) for A_mat0_col in zip(*A_mat0)] for A_mat_T0_row in A_mat_T0]
ATy0 = A_mat_T0.dot(z_mat0)
ATA_inv0 = np.linalg.inv(ATA0)

a0 = ATA_inv0.dot(ATy0)
# z = a0 + a1x +a2y

x0 = np.outer(np.linspace(-1000, -600, 30), np.ones(30))
y0 = x0.copy().T    # transpose
z0 = a0[0] + a0[1]*x0 + a0[2]*y0

parameter = int(input('Which snapshot do you want to observe '))

alpha_lst =[]

i = 0
x_value_lst = []
y_value_lst = []
z_value_lst = []
time_lst = []

while i < 20001:
    if data[parameter][i][0] < int(-1):
        x_value_lst.append(data[parameter][i][0])
        y_value_lst.append(data[parameter][i][1])
        z_value_lst.append(data[parameter][i][2])
        time_lst.append(times[i])
        i += 1
    else:
        i += 1


A_mat = np.zeros((int(len(x_value_lst)),3))
z_mat = np.zeros(int(len(x_value_lst)))

for j in range(len(x_value_lst)):
    A_mat[j][0] = 1
    A_mat[j][1] = x_value_lst[j]
    A_mat[j][2] = y_value_lst[j]
    z_mat[j] = z_value_lst[j]


A_mat_T = A_mat.transpose()
ATA = [[sum(a*b for a,b in zip(A_mat_T_row,A_mat_col)) for A_mat_col in zip(*A_mat)] for A_mat_T_row in A_mat_T]
ATy = A_mat_T.dot(z_mat)
ATA_inv = np.linalg.inv(ATA)

a = ATA_inv.dot(ATy)
# z = a0 + a1x +a2y


x = np.outer(np.linspace(-1000, -600, 30), np.ones(30))
y = x.copy().T # transpose
z = a[0] + a[1]*x + a[2]*y

cos_alpha =  abs(a0[1]*a[1]+a0[2]*a[2]+1*1) / (sqrt(a0[1]**2+a0[2]**2+1**2)*sqrt(a[1]**2+a[2]**2+1**2))

alpha = acos(cos_alpha)
print(cos_alpha)
print('angle between two planes is: ', degrees(alpha))
print(a0,a)

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot_surface(x, y, z,cmap='viridis', edgecolor='none')
ax.plot_surface(x0, y0, z0,cmap='gray',edgecolor='none')
ax.set_title('Linear regression of airfoil')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

plt.show()
