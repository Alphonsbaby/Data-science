import numpy as np
x = np.array([[2, 4, 6,1], [6, 8, 10,1],[1, 2, 1,1], [1, 1, 1,1]])
print(x)
print("Display all elements excluding the first row")
print(x[1:])

print("Display all elements excluding the last column")
print(x[:, :3])

print("Display the elements of 2 nd and 3 rd column")
print(x[:, 1:3])

print("Display the elements of 1 st and 2 nd column in 2 nd and 3 rd row")


print("Display 2 nd and 3 rd element of 1 st row")
print(x[0,1])
print(x[0,2])

