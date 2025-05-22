x, y, z = 3, 5, 7
print(x)
print(y)
print(z)

x = y = z = 5
print(x)
print(y)
print(z)

# If you have a collection of values in a list, tuple etc. Python allows
#  you to extract the values into variables. This is called unpacking.
cars = ["Toyota", "Audi", "Ferrari"]
x,y,z = cars
print(x)
print(y)
print(z)

x=str(567)
print(type(x))

# Output using +
print(x + y + z)
# print(67 + y) #TypeError: unsupported operand type(s) for +: 'int' and 'str' 
# Solution -> use ,
print(67,y)

# Global Vars
x="Hello"

def fun1():
    global x
    x = "Changed"
fun1()

print(x)