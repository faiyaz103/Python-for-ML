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

# Join 2 lists

# + operator
list1=[1,2,3]
list2=[4,5,6]
list3=list1 + list2
print(list3)

# Append Items. To add an item to the end of the list, use the 
# append() method:
myList.append("bhua")
print(myList)

# Add Any Iterable. The extend() method does not have to append lists, you 
# can add any iterable object (tuples, sets, dictionaries etc.).
thisTuple=("mangoes", "Melons")
myList.extend(thisTuple)
print(myList)

# remove specified items
# If there are more than one item with the specified value, the remove() 
# method removes the first occurrence:
myList.remove("kola")
print(myList)

# The pop() method removes the specified index.
# If you do not specify the index, the pop() method removes the last item.
myList.pop(1)
print(myList)

# The del keyword also removes the specified index:
# The del keyword can also delete the list completely: del myList
del myList[0]
print(myList)

# The clear() method empties the list.
# The list still remains, but it has no content.
myList.clear()
print(myList)

# Copy a List
fruits=['banana','pear','fig']
sell=fruits.copy()
print(sell)

buy=list(sell)
print(buy)