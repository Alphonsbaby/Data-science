import numpy as np

M1 = np.array([[3, 6], [14, 21]])
M2 = np.array([[9, 27], [11, 22]])
M3 = M1 + M2  
print("Matrix addition")
print(M3)
M1 = np.array([[3, 6], [14, 21]])
M2 = np.array([[9, 27], [11, 22]])
M3 = M1 - M2  
print("Matrix Substract")
print(M3)

M1 = np.array([[3, 6], [14, 21]])
M2 = np.array([[9, 27], [11, 22]])
M3 = M1 / M2  
print("Divide the elements of the matrices")
print(M3)


M1 = np.array([[3, 6], [5, -10]])
M2 = np.array([[9, -18], [11, 22]])
M3 = M1 * M2
print("Multiply the individual elements of matrix") 
print(M3)


M1 = np.array([[3, 6], [5, -10]])
M2 = np.array([[9, -18], [11, 22]])
M3 = M1.dot(M2) 
print("matrix multiplication") 
print(M3)

M1 = np.array([[3, 6, 9], [5, -10, 15], [4,8,12]])
M2 = M1.transpose()
print("Transpose of the matrix") 
print(M2)

M1 = np.array([[3, 6, 9], [5, -10, 15], [4,8,12]])
print("Sum of diagonal elements of a matrix") 
print(np.trace(M1))



