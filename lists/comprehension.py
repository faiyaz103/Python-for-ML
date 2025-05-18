# List comprehension offers a shorter syntax when you want to create a new 
# list based on the values of an existing list.

# Without list comprehension
oldList=['mangoes', 'banana', 'kiwi']
newlist=[]
for i in oldList:
    if 'a' in i:
        newlist.append(i)

print(newlist)

# The Syntax
# newlist = [expression for item in iterable if condition == True]
newnewList=[i for i in oldList if 'n' in i]
print(newnewList)