import numpy as np
A = np.array([[6, 1, 1,6,3],
              [4, -2, 5,1,3],
              [2, 8, 7,7,8],
              [6, 1, 1,6,3],
              [2, 8, 7,7,8]])
B=np.array([[2, 1, -2],
              [3, 0, 1],
              [1, 1, -1]])
print("Mat A=\n",A)
print("Mat B=\n",B)
C=A[:3, :3]
res = np.dot(B,C)
print("Multiplication Result\n",res)
A[:3,:3]=res[:3,:3]
print("Resultant Matrix:\n",A)

