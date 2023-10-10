import numpy as np

#join array-merges two arrays
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
ar = np.concatenate((v1,v2))
print(ar) #Merged Array

#2-D Array
v1 = np.array([[1,2],[3,4]])
v2 = np.array([[5,6],[7,8]])
ar_new = np.concatenate((v1,v2),axis = 0)
#Adding arrays along row as axis = 0
print(v1)
print()
print(v2)
print()
print(ar_new)
print()

#Stack function
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
c = np.stack((v1,v2))
c1 = np.hstack((v1,v2)) #row
c2 = np.vstack((v1,v2)) #column
c3 = np.dstack((v1,v2)) #height
print(c)
print()
print(c1)
print()
print(c2)
print()
print(c3)

#Split Function - used for splitting array

v1 = np.array([1,2,3,4,5,6])
print(v1)
spl = np.array_split(v1,3) #splits array into 3 arrays
print(spl)
print(type(spl)) #Lisr

# #Spliting along axis
v1 = np.array([[1,2],[3,4],[5,6]])
spl1 = np.array_split(v1,2,axis = 1)
print()
print(spl1)







