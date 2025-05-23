import numpy as np

# Splitting is reverse operation of Joining.
# array_split() for splitting arrays, we pass it the array we want to split 
# and the number of splits.

arr=np.array([1,2,3,4,5,6,7,8])

newarr=np.array_split(arr,3)
print(newarr)
newarr=np.array_split(arr,5)
print(newarr)
print(newarr[2])

# Splitting 2-D Arrays
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3) #split along the rows (axis=0).
print(newarr)
newarr = np.array_split(arr, 3, axis=1) #split along the columns (axis=1).
print(newarr)

#  alternate solution is using hsplit() opposite of hstack()
# Similar alternates to vstack() and dstack() are available as vsplit() and dsplit().