import numpy as np 
#rand()-Generates random numpy float nos. between 0 and 1.
var = np.random.rand(5)
print(type(var[1]))
print(var)

var1 = np.random.rand(2,5)  #Creates array of 2x5 of elements btw 0 and 1
print(var1)

#randn()-Generates random number close to 0.May return Positive or Negative numbers as well.
var2 = np.random.randn(5)
print(var2)

#ranf()-Generates random nos between 0 and 1,including 0 and not including 1
var3 = np.random.ranf(5)
print(var3)

#randint(min,max,total_no)-Generates random nos. between given two numbers
var4 = np.random.randint(2,7,10)  #Generates no. between 2 and 5
print(var4)
