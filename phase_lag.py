import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.signal

#sorry for the horrible coding

print("Initialization")
defl_reg_1 = [0.66244971, 8.06168428, 0.1910992]
defl_reg_2 = [0.03223218, -3.9516562, 0.11505326]
# defl_reg_1 = [0, 8.06168428, 0.1910992]
# defl_reg_2 = [0, -3.9516562, 0.11505326]
a = 4
b = 0.001
x = np.arange(0, 2*math.pi*a, b)
y1_arr = np.arange(0, 2*math.pi*a, b)
y2_arr = np.arange(0, 2*math.pi*a, b)

y1_count = 0
y2_count = 0

print("---------------------")
print(f"a = {a},", f"b = {b}")
print("---------------------")
print("Running first loop...")

for x_loop in x:
    y1 = defl_reg_1[0] + (math.sin(x_loop) * (defl_reg_1[1])) + (math.cos(x_loop) * (defl_reg_1[2]))
    y1_arr[y1_count] = y1

    y2 = defl_reg_2[0] + (math.sin(x_loop) * (defl_reg_2[1])) + (math.cos(x_loop) * (defl_reg_2[2]))
    y2_arr[y2_count] = y2

    y1_count += 1
    y2_count += 1

print("✅")

y1_h = scipy.signal.hilbert(y1_arr)
y2_h = scipy.signal.hilbert(y2_arr)
phase_rad = abs(np.angle(np.divide(y1_h, y2_h)))

status1 = 0
incr = 0
decr = 1
status1_lst = []

print("Running second loop...")

for n in range(len(x)-1):
    if phase_rad[[n]] < phase_rad[[n+1]]:
        status1 = incr

    if phase_rad[[n]] > phase_rad[[n+1]]:
        status1 = decr

    status1_lst.append(status1)

print("✅✅")


status2 = 2
neg = 2
pos = 3
status2_lst = []

print("Running third loop...")

for o in range(len(x)-2):
    if phase_rad[[o]] > 3.0500:
        if (status1_lst[o] - status1_lst[o+1])==-1:
            if status2 == 2:
                status2 = pos
            elif status2 == 3:
                status2 = neg
    status2_lst.append(status2)

#status1_lst[o] != status1_lst[o+1] and status1_lst[o] > status1_lst[o+1]

print("✅✅✅")
print("Running fourth loop...")

for p in range(len(x)-2):
    if status2_lst[p] == 3:
        correction = (2*math.pi) - phase_rad[[p]]
        phase_rad[[p]] = correction
    else:
        continue

print("✅✅✅✅ => plot")
print(f"Test --- {y2_h[[0]]}")
# print(status1_lst)
# print(status2_lst)

#version with only the phase lag
fig, ax = plt.subplots()
ax.plot(x, phase_rad, '#003366')
ax.set_xlabel('time [rad]')
ax.set_ylabel('phase lag [rad]')
plt.hlines(math.pi, 0, 2*math.pi*a, colors=None, linestyles='dotted')
#ax.set_title('A single plot')

plt.show()

def deg2rad(x):
    return x * np.pi / 180


def rad2deg(x):
    return x * 180 / np.pi

# #version with all plots (old)
# fig, ax1 = plt.subplots()
# ax2 = ax1.twinx()
# ax1.plot(x, y1_arr, 'dodgerblue')
# ax1.plot(x, y2_arr, 'orange')
# ax2.plot(x, phase_rad, '#003366')
# ax1.set_xlabel('time [rad]')
# ax1.set_ylabel('angle of attack/deflection [deg]')
# ax2.set_ylabel('phase lag [rad]', color='#003366')

fig, (ax1,ax2) = plt.subplots(2, sharex=True)
ax1.plot(x, phase_rad, '#003366')
ax2.plot(x, y1_arr, 'dodgerblue')
ax2.plot(x, y2_arr, 'orange')
ax1.set_ylabel('phase lag [rad]')
ax1.hlines(math.pi, 0, 2*math.pi*a, colors=None, linestyles='dotted')
ax1.grid(b=None, which='major', axis='both')
ax2.set_xlabel('time [rad]')
ax2.set_ylabel('angle [deg]')
ax2.grid(b=None, which='major', axis='both')

plt.show()


