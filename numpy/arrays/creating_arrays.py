import numpy as np

arr = np.array([1,2,3,4,5])
# we can pass a list, tuple or any array-like object into the array() method,
#  and it will be converted into an ndarray:
print(arr)
print(type(arr))

# A dimension in arrays is one level of array depth (nested arrays).
# ndim attribute: number of dimensions the array have.
# 0-D Arrays
arr=np.array(23)
print(arr)
print(arr.ndim)
# 1-D Array
arr=np.array((2,4,5,1))
print(arr)
print(arr.ndim)
# 2-D Array
arr=np.array(((23,4,5,6),(1,4,5,9)))
print(arr)
print(arr.ndim)
# 3-D Array
arr=np.array((((23,4,5,6),(1,4,5,9)), ((23,4,5,6),(1,4,5,9))))
print(arr)
print(arr.ndim)

# An array can have any number of dimensions.
# can define the number of dimensions by using the ndmin argument.
arr=np.array((1,2,3,4), ndmin=5)
print(arr)
print(arr.ndim)
# 1st Dimenstion: 4D array (Outmost)
# 2nd Dimenstion: 3D array
# 3rd Dimenstion: 2D array/matrix
# 4th Dimenstion: vector
# 5th Dimenstion: 4 elements (innermost)