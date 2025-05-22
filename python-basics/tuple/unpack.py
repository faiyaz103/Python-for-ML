# When we create a tuple, we normally assign values to it. This is called 
# "packing" a tuple:
# But, in Python, we are also allowed to extract the values back into 
# variables. This is called "unpacking":
fruits=('apple', 'orange', 'berry')
(green, yellow, blue) = fruits
print(green)
print(yellow)
print(blue)

# The number of variables must match the number of values in the tuple, 
# if not, you must use an asterisk to collect the remaining values as a list.
fruits=('apple', 'orange', 'berry', 'cherry', 'strawberry', 'pear')
(green, yellow, blue, *red) = fruits
print(green)
print(yellow)
print(blue)
print(red)

(start, *green, yellow, red) = fruits
print(start)
print(green)
print(yellow)
print(red)
