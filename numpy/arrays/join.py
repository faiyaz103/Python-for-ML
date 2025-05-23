import numpy as np

# Joining means putting contents of two or more arrays in a single array.
# in NumPy we join arrays by axes.
# We pass a sequence of arrays that we want to join to the concatenate() 
# function, along with the axis. If axis is not explicitly passed, it is 
# taken as 0.
arr1=np.array([3,5,6])
arr2=np.array([90,87,34])
# axis 1 is out of bounds for array of dimension 1, axis=0 is by default without mentioning
arr3=np.concatenate((arr1,arr2), axis=0)
print(arr3)

# 2D: axis=0,1
arr1=np.array([[34,56], [76,2]])
arr2=np.array([[3,6], [7,21]])

arr=np.concatenate((arr1,arr2))
print(arr)

arr=np.concatenate((arr1,arr2),axis=1)
print(arr)

# Joining Arrays Using Stack Functions
#  same as concatenation, the only difference is that stacking is done along a new axis.
# We can concatenate two 1-D arrays along the second axis which would result 
# in putting them one over the other, ie. stacking.
# If axis is not explicitly passed it is taken as 0.
arr1=np.array([3,5,6])
arr2=np.array([90,87,34])

arr=np.stack((arr1,arr2))
print(arr)
arr=np.stack((arr1,arr2),axis=1)
print(arr)

# NumPy provides a helper function: hstack() to stack along rows.
arr=np.hstack((arr1,arr2))
print(arr)
# NumPy provides a helper function: vstack()  to stack along columns.
arr=np.vstack((arr1,arr2))
print(arr)
# NumPy provides a helper function: dstack() to stack along height, which is the same as depth.
arr=np.dstack((arr1,arr2))
print(arr)