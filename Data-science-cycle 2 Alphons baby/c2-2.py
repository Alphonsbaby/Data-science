import numpy as np

matrix=np.random.randint(0,10,4).reshape(2,2)
print("Display the cube of each element of the matrix using different methods (use multiply(),*, power(),**)")
x=np.power(matrix,3)
print("power()",x)
y=np.multiply(matrix,(matrix*matrix))
print("multiply()")
print(y)
z=matrix*matrix*matrix
print("**")
print(z)
cube=matrix*3
print("*")
print(cube)
print("Display identity matrix of the given square matrix.")
identity=np.identity(2,dtype=int)
print(identity)
print("Display each element of the matrix to different powers.")
dpow=np.power(matrix,matrix)
print(dpow)
print("Create a matrix Y with same dimension as X and perform the operation X^2 +2Y")
a=np.add((np.power(x,2)),(np.multiply(y,2)))
print(a)