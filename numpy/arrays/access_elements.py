import numpy as np

# 2D
arr=np.array(((3,4,1,5),(7,3,19,0)))
print(arr[1,2])
# Negative Indexing
print(arr[0,-1])

# 3D
arr=np.array((((3,4,1,5),(7,3,5,0)), ((12,4,14,67),(43,87,90,31))))
print(arr[1,0,2])

