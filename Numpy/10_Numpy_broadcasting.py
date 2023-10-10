import numpy as np
var1 = np.array([1,2,3,4])

# print(var1 + var2) #Gives Broadcast error as no. of elements are not equal in both arrays.
# Broadcasting rule states that dimension of arrays must be same for add and subtract.
# If we have different dimensions,then atleast one array must have same value
print(var1.shape) #1x4 array
print()
var2 = np.array([[1],[2],[3]])
print(var2)
print(var2.shape) #3x1

print("Var1 + Var2 :",var1 + var2) #It will give array of max no. from both arrays i.e. 3x4 matrix(array).

x = np.array([[1],[2]])
print(x.shape) #2x1 One of column must be 1 in array.

x1 = np.array([[1,2,3],[4,5,6]])
print(x1.shape) #2x3
print()
print("X + X1:",x + x1)


