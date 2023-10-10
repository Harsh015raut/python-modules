import numpy as np
#For 1-D Array
#Note:Array index always starts at 0
x = np.array([1,2,3,4])
print(x[1]) #will print 2

#For 2-D Array
x1 = np.array([[1,2],[3,4]])
print(x1)
#[[1 2]
#[3 4]]
#Here [1,2] is a an 0th row(element) of our array and hence index of [1,2] will be 0.
#Similarly index of [3,4] will be 1.
#We can again do indexing in this list inside array also normaly.

#Now for accessing 2 in x1
print(x1[0][1])#->prints 2   #Here i indexed thorugh the array first,and then the list.
#Negative index also works for numpy arrays similarly to  list.
print(x1[-2][1])  #It will also print 2

#For 3-D Array

var2 = np.array([[[1,2],[3,4]]])
print("3-D Array:\n",var2)

#For accessing 3 from our array,we will slice through all 3 dimensions.
print(var2[0][1][0]) #First arrays 0th row contains our arrays
# first [0] represent first array inside,[1] represents 2nd list of this array,[0] represents the index of 3 in that list

# SLICING
s = np.array([1,2,3,4,5])
#Slicing in array works similar to slicing of List
#s[start_value:stop_value:step]
print(s[0:5:1])  #Will print Whole array

#Now i want to get 2,3,4
print("From 2 to 4:",s[1:4])

# for printint all elements
print("Printing all elements:",s[:])

#using step function
print("Skipping 1 element:",s[::2])


#For 2-D Array
s = np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(5-9)
print("Printing 5 to 9:",s[1,1:],s[2,:])

