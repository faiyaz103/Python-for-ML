# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.
import basicmodule
basicmodule.greeting("Faiyaz")

# You can create an alias when you import a module, by using the as keyword:
import personmodule as p
age=p.person["age"]
print(age)

# Built-in Modules
import platform
x=platform.system()
print(x)
# The dir() function:
# built-in function to list all the function names (or variable names) in a 
# module.
y=dir(platform)
print(y)

# You can choose to import only parts from a module, by using the from keyword.
from garagemodule import cars
for x in cars:
    print(x)
