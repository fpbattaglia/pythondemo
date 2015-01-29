__author__ = 'fpbatta'


import numpy as np


# in matlab you would say a = [1, 2, 3, 4];
a = np.array([1, 2, 3, 4])
# notice no semicolon!

print a
# in python 3: print(a)

b = np.array([5, 4, 3, 2])

a_matrix = np.array([[12, 3, 6, 2],
                     [9, 11, 5, 8],
                     [1, 0, 5, 3]])

print a_matrix * 3
print a_matrix.shape


# this is equivalent to a .* b
print a * b

a_tuple = (32, 'goodbye', (3, 4))

