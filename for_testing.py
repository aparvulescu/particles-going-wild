import numpy as np

A = np.array([[1, 2], [3, 4]])

AT = A.transpose()
ATA = AT.dot(A)
        
print(ATA)

