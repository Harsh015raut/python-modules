import numpy as np
#Iterations
#1-D Array

v1 = np.array([5,7,4,2,9,1])
print(v1)
print()
for i in v1:
    print(i,end = ",")

#For 2-D Array
v2 = np.array([[1,2,3],[4,5,6]])
print(v2)
print()
for i in v2:
    for j in i:
        print(j,end=',') #Prints elements of 2-D Array
print()
#For 3-D

v3 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(v3)
print()
for i in v3:
    for j in i:
        for k in j:
            print(k,end = ',')

#Jitne Dimensions Utne Loops

#For iterating in just 1 line we use- nditer()
#3-D Array

v3 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(v3)
print()
for i in np.nditer(v3,flags=['buffered'],op_dtypes=['S']):
    print(i,end = ',')


#np.nditer(v3,flags=['buffered'],op_dtypes=['S']) stores values in buffer,op_dtypes = 's' mean to be saved in string  format

#ndenumerate() - provides index of itereated value.
for i,d in np.ndenumerate(v3):
    print(i,d)