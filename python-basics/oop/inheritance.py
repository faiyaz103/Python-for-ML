class Person:
    def __init__(self,fname='John',lname='Doe'):
        self.fname=fname
        self.lname=lname
    
    def printname(self):
        print(self.fname, self.lname)

p1=Person('Amy','Admas')
p1.printname()

# Create a Child Class
# Use the pass keyword when you do not want to add any other properties or 
# methods to the class.
class Student(Person):
    pass

stud1=Student('Drake','Ramoroy')
stud1.printname()

# The child's __init__() function overrides the inheritance of the 
# parent's __init__() function.
class Teacher(Person):
    def __init__(self,fname, lname):
        self.fname=fname
        self.lname=lname

teacher=Teacher("Rosie","Jones")
teacher.printname()

# To keep the inheritance of the parent's __init__(),  a super() function 
# that will make the child class inherit all the methods and properties from 
# its parent
class Staff(Person):
    def __init__(self, fname='John', lname='Doe'):
        super().__init__(fname, lname)

staff=Staff()
staff.printname()

# Add Properties
class Guard(Person):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname)
        self.age=age
    
    def welcome(self):
        print("Welcome")

guard=Guard("Lea","Log",43)
guard.printname()
guard.welcome()
# If you add a method in the child class with the same name as a function in 
# the parent class, the inheritance of the parent method will be overridden.