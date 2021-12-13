import numpy as np
A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])
  
inv=np.transpose(A)
print (inv)
neg=np.negative(A)
comparison = A == inv
comparison1 = inv== neg
equal_arrays = comparison.all()
skew=comparison1.all()
if equal_arrays :
    print("Symmetric")
else:
    print("not Symmetric")
    
if skew:
    print("Skew Symmetric")
else:
    print("Not Skew Symmetric")
