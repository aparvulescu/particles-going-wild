# Algorithm for the visualisation of the 3D positions of the paticles in time

file_no = input("Select .dat file to import [integer between 0 and 2]: ")

f = open("data\Case" + str(file_no) + ".dat", 'r')

snapshot = -1
no_part = 0
time = -1

for line in f.readlines():
    if line.startswith("TITLE") or line.startswith("VARIABLES") or line.startswith("DATAPACKING"):
        pass
    if line.startswith("ZONE"):
        # snapshot = int(line[17:20]) <- to be fixed with str.split(sep)
        pass
    if line.startswith("STRANDID"):
        # time = float(line[26:]) <- to be fixed with str.split(sep)
        print(time)
        

f.close()

a = "house"
print(a[2:-1])
