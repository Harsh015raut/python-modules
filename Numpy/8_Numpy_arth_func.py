import numpy as np
#Arithmetic Fucntions
var = np.array([1,2,3,4,5,6,7,8,9,10])

#np.min
print("Minimum value is:",np.min(var))

#np.max
print("Minimum value is:",np.max(var))

#np.argmin - gives position of min
print("Minimum value is:",np.max(var),np.argmin(var))

#For 2-D array
var1 = np.array([[1,2,3],[4,5,6]])
print("Min value across column is:",np.min(var1,axis = 0))
print("Min value across row is:",np.min(var1,axis = 1))


#np.sqrt - used for squareroot
print("Square root:",np.sqrt(var1))

#np.sin
var2 = np.array([1,2,3])
print(np.sin(var2))
#np.cos
print(np.cos(var2))

#np.cumsum - cummulative sum similar to cf

print(np.cumsum(var2))