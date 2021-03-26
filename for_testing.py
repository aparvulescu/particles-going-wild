import numpy as np

file_no = 0

track_id_file = open(f"data\TrackIDUpdate{file_no}.dat", 'r')

marker_tid_list = []

for line in track_id_file.readlines():
    marker_tid_list.append([])
    numbers = line.split(' ')
    numbers.remove('\n')
    for number in numbers:
        marker_tid_list[-1].append(int(number))
        
print(marker_tid_list[0])

