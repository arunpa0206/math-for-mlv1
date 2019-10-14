
import numpy as np
m = np.matrix([[1, 0, 0], 
               [1, 1, 0], 
               [0, 0, 1]])
eigenvalues, eigenvectors = np.linalg.eig(m)
print (eigenvalues)
print (eigenvectors)