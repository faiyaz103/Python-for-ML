# A tuple is a collection which is ordered, unchangeable and allow duplicate values.
# Tuples are written with round brackets.
# items have a defined order, and that order will not change.
# we cannot change, add or remove items after the tuple has been created.
# tuples are indexed, they can have items with the same value:

thisTuple=('banana', 3, 4.5, 'a', 'hotash')
print(thisTuple)

print(len(thisTuple))

# One item tuple, remember the comma
newTuple=('kola') #<class 'str'>
print(type(newTuple))

newTuple=('kola',) #<class 'tuple'>
print(type(newTuple))


# Access Tuple Items

print(thisTuple[2])
print(thisTuple[-3])
# Range of Indexes
print(thisTuple[1:4])
print(thisTuple[:3])
print(thisTuple[2:])
print(thisTuple[-3:-1])

# Check if Item Exists
if 'banana' in thisTuple:
    print('yes')

# UPDATE TUPLES
# Tuples are unchangeable, To change, add or remove items from tuple:
# 1. Convert it into a list
# 2. Make changes in the list
# 3. Convert the list into tuple
conList=list(thisTuple)
conList[0]='berry'
conList.append('orange')
conList.remove(4.5)
thisTuple=tuple(conList)
print(thisTuple)

# Add tuple to a tuple.
newTuple=('audi', 'bmw')
thisTuple+=newTuple
print(thisTuple)

# Multiply Tuples
newTuple=newTuple*2
print(newTuple)