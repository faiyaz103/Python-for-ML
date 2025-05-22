# [start:end]
# [start:end:step]
import numpy as np

# Use the step value to determine the step of the slicing:
arr=np.array((1,2,3,4,5,6,7,8,9,10))
print(arr[1:7:2])
print(arr[:8:2])
print(arr[3::2])
print(arr[::3])

# 2D array
arr=np.array(((1,2,3,4),(5,6,7,8)))
print(arr[1,1:3])
# From both elements, return index 2:
print(arr[0:2,1])
# From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
print(arr[0:2,1:3])