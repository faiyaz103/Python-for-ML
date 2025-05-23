# NumPy offers the random module to work with random numbers.
from numpy import random

# Generate a random integer from 0 to 100:
x=random.randint(100)
print(x)

# Generate Random Array
# The randint() method takes a size parameter where you can specify the shape 
# of an array.

# 1D
x=random.randint(100, size=(5))
print(x)
# 2D
x=random.randint(100, size=(3,5))
print(x)

# rand() method returns a random float between 0 and 1.
x=random.rand()
print(x)

# The rand() method also allows you to specify the shape of the array.
x=random.rand(5)
print(x)
# 2-D array with 3 rows, each row containing 5 random numbers:
x=random.rand(3,5)
print(x)

# Generate Random Number From Array
x=random.choice([2,45,1,5])
print(x)
# The choice() method also allows you to return an array of values.
# Add a size parameter to specify the shape of the array.
x=random.choice([2,45,1,5], size=(3))
print(x)
x=random.choice([2,45,1,5],size=(3,5))
print(x)


