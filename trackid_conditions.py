import numpy as np
from data_gathering import get_data

#SUMMARY:
#goal; update initial grid with new track-IDs for each snapshot
#for each track-ID in initial snapshot t_0 look for most close neighbour in both x,y,z directions in snapshot t_1
#add some conditions when the found track-ID is not the closest in all three directions
#assign the found track-ID to the grid

#CRITICAL POINTS:
#when a marker is found that wasn't in the grid earlier what to do.


