#difference between numpy dot() and inner()
#What's difference between numpy dot() and inner()?

#Let's look into 2D array as an example:

import numpy as np
'''

a=np.array([1,2])
b=np.array([11,12])
print(np.dot(a,b))
print(np.inner(a,b))

#Numpy Matrices
A = np.matrix([[1.,2], [3,4], [5,6]])
print(A)

#Mathlab style
B = np.matrix("1.,2; 3,4; 5,6")
print(B)


#Vectors are handled as matrices with one row or one column:

x = np.matrix("10, 20")
print(x)

#Matrix Vector Multiplication
x = np.matrix("4.;5.")
print('X:',x)
A = np.matrix([[1.,2], [3,4], [5,6]])
print('A:',A)
print('A*x',A*x)

#Note that the rank of the array is not the rank of the matrix in linear algebra (dimension of the column space) but the number of subscripts it takes!
A = np.ones((4,3))
print(A)
print(np.rank(A))

#Scalars have rank 0:
x = np.array(10)
print(x)
print(np.rank(x))
'''
#Dot product of two Vectors
A = np.array([[1,2],[3,4]])
print(A)

b = np.array([10, 20])
print(b)

ans = np.dot(A,b)
print(ans)




#Matr
