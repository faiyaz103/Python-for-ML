import numpy as np
from numpy import random

# Shuffling Arrays
# The shuffle() method makes changes to the original array.
arr=np.array([23,5,3,78])
random.shuffle(arr)
print(arr)

# Generating Permutation of Arrays
# The permutation() method returns a re-arranged array (and leaves the 
# original array un-changed).
arr=np.array([1,2,3,4,5,6])
print(random.permutation(arr))