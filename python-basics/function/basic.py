def add(num1, num2):
    print(num1+num2)

add(3,6)

# Arbitrary Arguments
# For unknown number of arguments, add a * before the parameter name
# the function will receive a tuple of arguments, and can access the items accordingly
def func(*values):
    print("2nd value is " + str(values[1]))

func("ABCD", 32, "DEG")

# Keyword Arguments
# You can also send arguments with the key = value syntax.
def name(lastname, firstname):
    print("First name: "+firstname+" Last name: "+lastname)

name(firstname='Faiyaz', lastname='Mahmud')

# Arbitrary Keyword Arguments, **kwargs
def name(**name):
    print("First name: "+name['firstname']+" Last name: "+name['lastname'])

name(firstname='Faiyaz', lastname='Mahmud')

# Default Parameter Value
def color(colorname="white"):
    print(colorname)

color()
color("Blue")

# You can send any data types of argument to a function (string, number, list, dictionary etc.)
def garage(cars):
    for car in cars:
        print(car)
    return cars[1]
    
cars=['audi','bmw','volvo']
latest=garage(cars)
print(latest)

# function definitions cannot be empty
def myfunction():
    pass