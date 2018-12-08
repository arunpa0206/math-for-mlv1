import numpy as np
from numpy.linalg import eig

A = np.array([[1,2],[3,4]])
print(eig(A))

#The eig returns two tuples: the first one is 
