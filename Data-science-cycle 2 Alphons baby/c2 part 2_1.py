import numpy as np
import numpy as nf
from numpy.linalg import eig
mat = np.random.randint(10, size=(3, 3))
array = nf.random.randint(10, size=(3, 3))
print(mat)

M_inverse = np.linalg.inv(mat)
print("inverse of the array")
print(M_inverse)

rank = np.linalg.matrix_rank(mat)
print("Rank of the given Matrix ")
print(rank)

det= np.linalg.det(mat)
print("determinant of the given Matrix ")
print(det)

arr=mat.flatten()
print("transform matrix to array ")
print(arr)

w,v=eig(array)
print('E-value:', w)
print('E-vector', v)

