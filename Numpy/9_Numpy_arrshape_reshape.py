import numpy as np

#Shape of Array - Gives the rowsxcolumns of a array.

var1 = np.array([[1,2],[2,4]])
print(var1)
print("Shape of array is:",var1.shape)

var2 = np.array([[1,2,3,4],[2,4,6,8]])
print("Shape of array is:",var2.shape)

#For making Multidimensional array,we pass ndmin= no. of dimensions

var1 = np.array([1,2,3,4],ndmin = 4)
print(var1)
print(var1.ndim)
print(var1.shape)

#Reshape - Making 1-D array to Multidimension array n vice- versa.
var2 = np.array([1,2,3,4,5,6]) 
print(var2,end="\n") #1-D Array
x = var2.reshape(2,3) #After reshaping all columns and rows of array must be filled
print(x)
print(x.ndim)  #2-D Array

#3-D Array

var3 = np.array([1,2,3,4,5,6,7,8,9])
print(var3)

#Reshaping it into 3x3 Array
x = var3.reshape(3,3)
print(x)


var3 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(var3)
x = var3.reshape(2,3,2)  #=> This means making 2 arrays of 2x3
print(x)

#Reconverting 3-D array to 1-D array
print(x.reshape(-1)) #-1 converts 3d array to 1-d array.


