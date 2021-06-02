import numpy as np
from data_gathering_update import get_data

file_no = 2

data, values, track_id_per_snapshot = get_data(file_no)

print(np.max(data[:, :, 6]))
