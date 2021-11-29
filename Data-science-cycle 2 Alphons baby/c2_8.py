import numpy as np

arr1 = np.arange(10, 16)
print("1D ARRAY ")
print("The array is: ", arr1)

obj = 2
value = 40

arr = np.insert(arr1, obj, value, axis=None)

print("After inserting the new array is: ")
print(arr)
print("Shape of the new array is : ", np.shape(arr))

print("2D ARRAY ")
arr1 = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9), (50, 51, 52)])

print("The array is: ")
print(arr1)
print("The shape of the array is: ", np.shape(arr1))

a = np.insert(arr1, 1, [[50], [100], ], axis=0)

print("New array is : ")
print(a)
print("Shape of the array is: ", np.shape(a))