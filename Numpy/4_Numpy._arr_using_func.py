import numpy as np
#Zero Array-All elements of this array are zero
ar1 = np.zeros(4)   #Gives array of 4 elements,each 0
print(ar1)


#size is used for making a array of our size

ar2 = np.zeros((3,4))   #Gives array of 12(3x4)Matrix elements,each 0
print(ar2)

#Array of ones-np.ones
ar3 = np.ones(5)
print(ar3)

#Empty Array

ar4 = np.empty(4)
print(ar4)

#Array of Range of a Value
ar5 = np.arange(5)
print(ar5)

#Array of diagonal 1's identity matrix

ar6 = np.eye(3)   #Creates array of 3x3
print(ar6)

ar7 = np.eye(3,5)
print(ar7) #Array of 3 Rows and 5 Columns

#linspace-Random elements between range,including both start and end index value
ar8 = np.linspace(1,10,num=5)
print(ar8)

 