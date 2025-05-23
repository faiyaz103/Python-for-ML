import numpy as np

# The function nditer() is a helping function that can be used from very basic
#  to very advanced iterations
arr=np.array([[[5,6],[7,8]], [[1,2],[3,4]]])
# NO need for nested loops
for x in np.nditer(arr):
    print(x)

# Iterating Array With Different Data Types
# use op_dtypes argument and pass it the expected datatype to change the 
# datatype of elements while iterating.
# NumPy does not change the data type of the element in-place (where the 
# element is in array) so it needs some other space to perform this action, 
# that extra space is called buffer, and in order to enable it in nditer() 
# we pass flags=['buffered'].
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)

# Iterating With Different Step Size
for x in np.nditer(arr[:,::2]):
    print(x)

# we require corresponding index of the element while iterating, the 
# ndenumerate() method can be used for those usecases.
for indx,x in np.ndenumerate(arr):
    print(indx,x)
