import numpy as np
a= np.array([[3, 6,7,8]])
b=np.array([[3, 6,8,7], [4, 2,1,0],[3,1,3,3],[1,1,2,2]])
x=np.diag(a)
y=np.diag(b)
print(x)
print(y)