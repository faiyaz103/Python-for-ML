# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one 
# expression.

# lambda arguments : expression

x = lambda a,b,c : a+b+c
print(x(2,5,6))

# Say you have a function definition that takes one argument, and that 
# argument will be multiplied with an unknown number:

def myfunc(n):
    return lambda a : a*n

x = myfunc(3) #Unknown number will be multiplied by 3
print(x(11)) #Unknown number