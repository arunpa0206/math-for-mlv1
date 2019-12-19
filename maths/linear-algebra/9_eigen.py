import numpy as np
from numpy.linalg import eig

A = np.array([[0,1],[-2,3]])
print(eig(A))

#The eig returns two tuples: the first one is
