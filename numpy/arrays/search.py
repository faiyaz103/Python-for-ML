import numpy as np

# You can search an array for a certain value, and return the indexes that get a match.
# To search an array, use the where() method.
arr=np.array([1,2,3,4,5,6,4,8,4])
x=np.where(arr==4)
print(x)
x=np.where(arr%2==0)
print(x)

# There is a method called searchsorted() which performs a binary search in 
# the array, and returns the index where the specified value would be inserted
#  to maintain the search order.
# used on sorted arrays.
arr=np.array([4,5,6,7,8,9,10])
x=np.searchsorted(arr,9)
print(x)
# By default the left most index is returned, but we can give side='right' 
# to return the right most index instead.
x=np.searchsorted(arr,9, side='right')
print(x)
# Multiple Values
x=np.searchsorted(arr,[1,3,11,15])
print(x)
# The return value is an array: [1 2 3] containing the three indexes where 
# 2, 4, 6 would be inserted in the original array to maintain the order.