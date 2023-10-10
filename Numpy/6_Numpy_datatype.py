import numpy as np
#.dtype - Gives data type of array elements
v1 = np.array([1,2,3,4])
print("Data Type :",v1.dtype) #int32
v2 = np.array([1.0,1.3,2.6])
print("Data Type :",v2.dtype) #float64
v3 = np.array(['A','B','C','D'])
print("Data Type :",v3.dtype)
v4 = np.array(['A','B','C','D',1,2,3])
print("Data Type:",v4.dtype)

#Changing datatype
x = np.array([1,2,3,4]) #Normal
print("Data Type",x.dtype)
#Changed
x = np.array([1,2,3,4],dtype = np.int8) #Changed
print("Data Type",x.dtype)

#Shortform
x1 = np.array([1,2,3,4],dtype ='f')
print("Data Type:",x1.dtype)
print(x1)

#Using Function as a function
x2 = np.array([3,4,5,6,7])
new = np.float32(x2) #converts x2 to float32
new_1 = np.int_(new) #COnverts new again to int
print(x2)
print(new)
print(new_1)
print("Data Type:",x2.dtype)
print("New Data Type:",new.dtype)
print("Data Type:",new_1)

#Directly Converting Datatypes
#astype - giving dtype
x3 = np.array([4,5,6,7])
new_1 = x3.astype(float) 
print("Data Type:",new_1.dtype)



