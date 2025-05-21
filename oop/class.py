# Basic
class MyClass:
    x=5

obj1 = MyClass()
print(obj1.x)

# The __init__() Function
# always executed when the class is being initiated.
# Use it to assign values to object properties, or other operations that are
#  necessary to do when the object is being created:
class Person:
    def __init__(self, name='John Doe', age=25):
        self.name=name
        self.age=age
    #The __str__() function controls what should be returned when the class
    #  object is represented as a string.
    def __str__(self):
        return f"{self.name} {self.age}" #formatted string
    
    # Object Method
    def intro(self):
        print("The name is "+ self.name)

p1=Person()
p2=Person('Peter',45)

print(p1.name)
print(p2.name)

p2.age=53
print(p2) # ifthe __str__() function is not set, the string representation of the object is returned
          #<__main__.Person object at 0x000001B1EB0FA090>

p2.intro()
