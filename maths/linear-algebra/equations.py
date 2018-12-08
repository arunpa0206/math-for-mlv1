import numpy as np

from numpy.linalg import solve

A = np.array([[1,2],[3,4]])
print(A)

b = np.array([10, 20])
print(b)
#A,x=b
x = solve(A,b)
print(x)
