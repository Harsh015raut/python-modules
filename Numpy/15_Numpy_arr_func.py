import numpy as np 
#Search Array
v1 = np.array([1,2,3,4,5,2,6,7,5])

#Where function- finds the tem we want to search
x = np.where(v1==2)
print(x)  #Gives index of 2 in our list

#Search sorted array
y = np.searchsorted(v1,5) #Tells us where in our sorted array will this number be placed
print(y)

y = np.searchsorted(v1,5,side = "right") #For searching from right
print(y)
# print(v1)

#Sorting an array
print(np.sort(v1))

#Filter Array 
vr = np.array(['a','b','c','d'])
f = [True,False,False,True]
new_a = vr[f]
print(new_a)






