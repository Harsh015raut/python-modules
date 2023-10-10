import numpy as np
v1 = np.array([1,2,3,4,5])
co = v1.copy() #Copy is made
print("V1 :",v1)
print("Copy:",co)

#View
v2 = np.arange(1,6)
vi = v2.view()
print("v2:",v2)
print("view:",vi)
#Copy is a new array
#View does not have any data
#If we change the view,then it will affect original array
#copy does not change original data
