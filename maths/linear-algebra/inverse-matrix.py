from numpy.linalg import inv
import numpy as np

a = np.array([[1., 2.], [3., 4.]])
ainv = inv(a)

print(ainv)
