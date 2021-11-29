import numpy as np

a = np.arange(0, 15, 2)
print(a)
print("Elements from index 2 to 8 with step 2")
s2 = slice(2, 8, 2)
print(a[s2])

print("Last 3 elements of the array using negative index",a[-3:-1])

print("Alternate elements of the array")

ab = np.arange(1, 15, 2)
print(ab)

print("Display the last 3 alternate elements",a[-3:-1:2])

