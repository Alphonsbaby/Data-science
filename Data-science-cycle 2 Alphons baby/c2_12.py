import numpy as np

a = np.array([1,2,8,9,3,4,5,6,7])
print(a)
array_copy = np.sort(a)[::-1]
print(array_copy[4:10])
