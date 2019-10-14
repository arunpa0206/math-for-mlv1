#derivative of y = x2+1
from sympy import *
import numpy as np
x = Symbol('x')
y = x**2 + 1
yprime = y.diff(x)
print(yprime)
