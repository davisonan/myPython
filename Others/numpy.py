# numpy.py
# numpy 

import numpy as np

a = arange(15).reshape(3, 5)
a.shape
a.ndim
a.dtype
a.dtype.name 
a.itemsize # number of bits for each item
a.size # number of items
type(a)

b = array([1.2, 2.3, 4.5])
b.dtype.name

c = array([(1.2, 2.3, 3.4), (2.0, 3.0, 3.0)])

c = array( [ [1,2], [3,4] ], dtype=complex )

a = np.zeros((2,2))
print a
b = np.ones((1,2))
print b
c = np.full((2,2), 7)
print c
d = np.eye(2)
print d
e = np.random.random((2,2))
print e

x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = x + v
print y
