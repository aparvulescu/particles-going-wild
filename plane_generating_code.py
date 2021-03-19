#hi guys it is so gezellig in here what is going on 
#gozer sie leoi ik proef kurk
#gadverdamme man
#jan-pieter
# 5 passenger business jet with red stripes. what does gezellig mean>?

#@andrei shall we just join forces because Sari and I arent smart enough for this (at least python)
# Alright, come here.


#I am sorry andrei i still have not included the datagathering definition because i suck at object oriented programming im way /
#too chaotic for that -- SL
# It's fine, we can maybe do it afterwarrds, or not at all if not needed
#yea sure, this one uses the data the same way s the other thing i wrote so we would only have to do it once for my stuff
# alrright, that's fine
#I would suggest we include these in-file conservations to the final report
#it really adds something
#it does man
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Algorithm for the visualisation of the 3D positions of the paticles in time

# file_no = input("Select .dat file to import [integer between 0 and 2]: ")
file_no = 1

f = open("data\Case" + str(file_no) + ".dat", 'r')

data = np.zeros((5001, 20001, 11))  # (snapshot, trackID, values)
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
    data[snapshot][tid][3] = values[4]  # x-velocity (u)
    data[snapshot][tid][4] = values[5]  # y-velocity (v)
    data[snapshot][tid][5] = values[6]  # z-velocity (w)
    data[snapshot][tid][6] = values[7]  # Speed magnitude (|V|)
    data[snapshot][tid][7] = values[9]  # x-acceleration (ax)
    data[snapshot][tid][8] = values[10]  # y-acceleration (ay)
    data[snapshot][tid][9] = values[11]  # z-acceleration (az)
    data[snapshot][tid][10] = values[12]  # acceleration magnitude (|a|)


f.close()

# parameter = int(input('Which snapshot do you want to observe'))
parameter = 2


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

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot_surface(x, y, z,cmap='viridis', edgecolor='none')
ax.set_title('Linear regression of airfoil')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')



plt.show()