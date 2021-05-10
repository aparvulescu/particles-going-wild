import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import math

# Algorithm for the visualisation of the 3D positions of the paticles in time
max_snapshot = [100, 3626, 3626]
f0 = 0.392  # [Hz]
dt = 0.01  # [s]
#file_no = 0  # input("Select .dat file to import [integer between 0 and 2]: ")

print("Gathering data. Please wait...")

file_angle = open("data\\aoa_graph_case1.dat", 'r')

for line in file_angle.readlines():
    angle_lst = np.array(list(map(float, line[:-1].split(' '))))

file_angle.close()

print("Finished gathering data! Now starting linear algebra.")

parameter = max_snapshot[2] 

t_arr = np.arange(0, dt*parameter, dt)
sin_arr = np.reshape(np.sin(2 * math.pi * f0 * t_arr), (parameter, 1))
cos_arr = np.reshape(np.cos(2 * math.pi * f0 * t_arr), (parameter, 1))
ones_arr = np.reshape(np.ones(parameter), (parameter, 1))

A_mat = np.hstack((ones_arr, sin_arr, cos_arr))
y_mat = np.reshape(angle_lst, (parameter, 1))

# print(y_mat)


number_of_outliers = 1
while number_of_outliers > 0:

    Qy = np.eye(int(A_mat.shape[0]))

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
        if e_norm[i] > 3:
            number_of_outliers += 1
            outliers_lst.append(i)
    
    A_mat = np.delete(A_mat, outliers_lst, 0)
    y_mat = np.delete(y_mat, outliers_lst, 0)
    



val = a[0] * np.ones(parameter) + a[1] * np.sin(2*math.pi*f0*t_arr) + a[2] * np.cos(2*math.pi*f0*t_arr)

print(a)

plt.plot(t_arr, angle_lst)
plt.plot(t_arr, val)
#plt.title('Angle of attack vs time for case 1')
plt.xlabel('Time [s]')
plt.ylabel('Angle of attack [degrees]')
plt.grid(True, which='both')
plt.show()
