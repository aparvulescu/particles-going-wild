import numpy as np

# Algorithm for the visualisation of the 3D positions of the paticles in time

file_no = input("Select .dat file to import [integer between 0 and 2]: ")

f = open("data\Case" + str(file_no) + ".dat", 'r')

data = np.zeros((5001, 20001, 16))  # (snapshot, trackID, values)
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
        print(f"Snapshot = {snapshot}")
        continue
    if line.startswith("STRANDID"):
        time = float(line.split('=')[2])
        times = np.append(times, time)
        print(f"Time = {time}")
        continue
    values = line.split(' ')
    # print(values)
    print(len(values))
    # id = values[8] # trackID

       

f.close()

print(times)

a = "house"
print(a[2:-1])
