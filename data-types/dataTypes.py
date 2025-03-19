# Python has a built-in module called random that can be used to make 
# random numbers:
import random

print(random.randrange(1,10))

# Int, or integer, is a whole number, positive or negative, without 
# decimals, of unlimited length.

# Float, or "floating point number" is a number, positive or negative, 
# containing one or more decimals.
# Float can also be scientific numbers with an "e" to indicate the power of 10.
x=32.56
print(x)
x=-87e-3
print(x)

# Complex
x=-5+7j
print(x, type(x))

# -----------Sequence Types------------
# List
x=["Apple", "Banana", "Cherry"]
print(x, type(x))

# Tuple
x=("Hi", "Hello", "What")
print(x, type(x))

x=range(7)
print(x, type(x))

# -----------Mapping Types--------------
#dict
x={"name": "john", "age": 45}
print(x, type(x))

# ----------Set Types-------------
# set
x={"hello", "how", "why"}
print(x, type(x))

# frozenset
x=frozenset({"apple", "orange"})
print(x, type(x))
# -------------------------------

# bytes
x=b"what"
print(x, type(x))

# bytearray
x=bytearray(4)
print(x, type(x))

# memoryview
x=memoryview(bytes(56))
print(x, type(x))

# none
x=None
print(x, type(x))

# setting specific data type
x = list(("apple", "banana", "cherry"))
print(x,type(x))

# Type Conversion
x=12
y=8.7
z=1j

a=float(x)
print(a,type(a))

a=int(y)
print(a,type(a))

a=complex(y)
print(a,type(a))
# You cannot convert complex numbers into another number type.
