import numpy as np
#np.add - addition in  arrays
x = np.arange(1,10)
x_add = x + 10
print(x_add)

#Adding two arrays
x1 = np.array([1,2,3])
x2 = np.array([4,5,6])
c = np.add(x1,x2)
print("The addition of 2 arrays is:",c)


#np.subtract - subtracts arrays
x = np.arange(1,10)
x_sub = x - 3
print(x_sub)

#Subtracting two arrays
x1 = np.array([1,2,3])
x2 = np.array([4,5,6])
c = np.subtract(x1,x2)
print("The subtraction of 2 arrays is:",c)

#np.multiply - multiplies arrays
x = np.arange(1,10)
x_multi = x * 10
print(x_multi)

#np.divide - divides arrays
x = np.arange(1,10)
x_divide = x / 10
print(x_divide)

x1 = np.array([1,2,3])
x2 = np.array([4,5,6])
c = np.divide(x1,x2)
print("The division of 2 arrays is:",c)

# np.mod - Gives mod
x = np.arange(1,10)
x_mod = x % 10
print(x_divide)

x1 = np.array([1,2,3])
x2 = np.array([4,5,6])
c = np.mod(x1,x2)
print("The remainder of 2 arrays is:",c)
# np.recipracal - 1/a = reciprocates
var = np.arange(1,5)
r = np.reciprocal(var)
print("Reciprocal is:",r)

#For 2-D Arrays

x1 = np.array([[4,5,6,],[1,2,3]])
x2 = np.array([[4,5,6,],[1,2,3]])
x_add = np.add(x1,x2)
print(x_add)


