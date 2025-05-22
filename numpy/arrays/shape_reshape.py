import numpy as np

# Shape of an Array
arr=np.array(((23,4,5,6),(1,4,5,9)))
print(arr.shape)
# (2, 4), which means that the array has 2 dimensions, where the first 
# dimension has 2 elements and the second has 4.
arr=np.array((1,2,3,4,5), ndmin=5)
print(arr.shape)

# Reshape From 1-D
arr=np.array((1,2,3,4,5,6,7,8,9,10,11,12))
newarr=arr.reshape(4,3)
print(newarr)
print(newarr.base) #reshaping returns a view

newarr3=newarr.reshape(2,3,2)
print(newarr3)
# Unknown Dimension
# you do not have to specify an exact number for one of the dimensions in the reshape method.
# Pass -1 as the value, and NumPy will calculate this number for you.
newarr2=newarr3.reshape(2,-1)
print(newarr2)
# Flattening array means converting a multidimensional array into a 1D array.
# We can use reshape(-1) to do this.
newarr1=newarr2.reshape(-1)
print(newarr1)