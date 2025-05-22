# Dictionaries are used to store data values in key:value pairs.
# ordered, changeable and do not allow duplicates.
thisDict={
    'brand': 'Audi',
    'model': 'X-8',
    'year': 2004,
    'colors': ['red', 'white', 'black']
}
print(thisDict)
print(thisDict['colors'])
print(len(thisDict))

# The keys() method will return a list of all the keys in the dictionary.
info=thisDict.keys()
print(info)
# The list of the keys is a view of the dictionary, meaning that any changes 
# done to the dictionary will be reflected in the keys list.
thisDict['origin']='Germany'
print(info)

# The values() method will return a list of all the values in the dictionary.
value=thisDict.values()
print(value)
# The list of the values is a view of the dictionary, meaning that any changes
#  done to the dictionary will be reflected in the values list.
thisDict['tax']='none'
print(value)

# The items() method will return each item in a dictionary, as tuples in a list.
item=thisDict.items()
print(item)
# The returned list is a view of the items of the dictionary, meaning that 
# any changes done to the dictionary will be reflected in the items list.

# Check if Key Exists
if 'tax' in thisDict:
    print('yes')

# Remove Dictionary Items
thisDict.pop('year')
print(thisDict)
# The popitem() method removes the last inserted item
thisDict.popitem()
print(thisDict)
# The del keyword removes the item with the specified key name
del thisDict['origin']
print(thisDict)

# Copy a Dictionary
newDic=thisDict.copy()
print(newDic)

another=dict(newDic)
print(another)

# The clear() method empties the dictionary:
thisDict.clear()
print(thisDict)