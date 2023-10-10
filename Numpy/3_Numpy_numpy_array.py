#Numpy Array
import numpy as np
a = np.array([1,2,3]) #Makes a 1-D Array
print(a)

#Types of Array
#ndim Function is used for getting dimension of the array

print("Dimension of array is :",a.ndim)

#2-D Array
ar2 = np.array([[1,2,3,4],[5,6,7,8]])
print(ar2)
print("Dimension of array is :",ar2.ndim)

#3-D Array
ar3 = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
print(ar3)
print("Dimension of array is :",ar3.ndim)

#Shortcut to create array of any dimension,we will use ndmin = no. of dimensions
ar4 = np.array([1,2,3,4,5],ndmin = 5)
print(ar4)
print("Dimension of array is :",ar4.ndim)