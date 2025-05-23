import numpy as np

# Getting some elements out of an existing array and creating a new array 
# out of them is called filtering.
# In NumPy, you filter an array using a boolean index list.
# If the value at an index is True that element is contained in the filtered array
# if the value at that index is False that element is excluded from the filtered array.
arr=np.array([1,2,45,6])
filt=[True,False,False,True]

newarr=arr[filt]
print(newarr)

# but the common use is to create a filter array based on conditions.
filt=[]

for x in arr:
    if x > 1:
        filt.append(True)
    else:
        filt.append(False)

newarr=arr[filt]
print(filt)
print(newarr)

# Creating Filter Directly From Array
filt= arr % 2==0
newarr=arr[filt]
print(newarr)