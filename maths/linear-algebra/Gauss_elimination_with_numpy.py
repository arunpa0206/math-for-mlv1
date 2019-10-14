import numpy.linalg
a = [[2, 9, 4], [7, 5, 3], [6, 1, 8]]
b = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
g=numpy.linalg.solve(a,b)
print(g)