import numpy as np
m = np.matrix([[2, -1, 0],
               [-1, 2, -1],
               [0, -1, 2]])

eigenvalues = np.linalg.eigvals(m)
print (eigenvalues)