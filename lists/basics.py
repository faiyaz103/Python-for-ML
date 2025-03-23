myList=["abc", 3, 'a', "abc", True, 4.90]
print(myList[2])

# Negative Indexing
print(myList[-1])

# Range of Indexes
print(myList[:2])

# Check if Item Exists
if "abc" in myList:
    print("YES")

# Change a Range of Item Values
myList[1:3]=["xyz", "pqr"] #['abc', 'xyz', 'pqr', 'abc', True, 4.9]
print(myList)

myList[1:3]=["lkj"] #['abc', 'lkj', 'abc', True, 4.9]
print(myList)

myList[1:3]=[3, 4, 5, 6] #['abc', 3, 4, 5, 6, True, 4.9]
print(myList)

# Insert Items. To insert a new list item, without replacing any of the 
# existing values, we can use the insert() method.
myList.insert(2,"kola") #['abc', 3, 'kola', 4, 5, 6, True, 4.9]
print(myList)

# Append Items. To add an item to the end of the list, use the 
# append() method:
myList.append("bhua")
print(myList)

# Add Any Iterable. The extend() method does not have to append lists, you 
# can add any iterable object (tuples, sets, dictionaries etc.).
thisTuple=("mangoes", "Melons")
myList.extend(thisTuple)
print(myList)