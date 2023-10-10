#Difference btw List and Array.
#In list we can store elements of all multiple datatypes.
#In numpy array we can use only one type of element.
#We can merge string and int for merging but we usually donot do it.
#Numpy array consumes less memory
#Numpy array perfrom numerical operations very fast and efficiently.
#We use numpy for Image Processing
#%timeit for
#%timeit 
import timeit
print(timeit.timeit [j**4 for j in range(1,9)])

# import numpy as np
# %timeit np.arange(1,9)**4