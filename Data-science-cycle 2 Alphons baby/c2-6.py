import numpy as np
A = np.array([[2, 1, -2],
              [3, 0, 1],
              [1, 1, -1]])
b=np.array([[3],
             [5],
             [-2]])
inv=np.linalg.inv(A)
x=np.linalg.solve(inv,b)
print(x)
