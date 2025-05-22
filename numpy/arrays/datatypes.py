import numpy as np

# dtype that returns the data type of the array
arr=np.array((1,2,3,4))
print(arr.dtype)

fruits=np.array(('apple','orange','palm'))
print(fruits)
print(fruits.dtype)

# Creating Arrays With a Defined Data Type
arr=np.array((1,2,3,4), dtype='S')
print(arr)
print(arr.dtype)
# Create an array with data type 4 bytes integer:
arr=np.array((1,2,3,4), dtype='i4')
print(arr)
print(arr.dtype)
# A non integer string like 'a' can not be converted to integer (will raise an error):
# arr=np.array(('a',2,3,4), dtype='i4')
# print(arr)
# print(arr.dtype)

# Converting Data Type on Existing Arrays
cg=np.array((3.4,2.9,4.0))
newarr=cg.astype('i8')
print(cg)
print(newarr)
print(newarr.dtype)