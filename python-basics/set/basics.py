# Unordered means that the items in a set do not have a defined order.
# Set items can appear in a different order every time you use them, and 
# cannot be referred to by index or key.

# Once a set is created, you cannot change its items, but you can remove items and add new items.Sets cannot have two items with the same value.

# Sets cannot have two items with the same value.
# True and 1 are considered the same value in sets
# False and 0 are considered the same value in sets
thisSet={'audi', 'banana', 123, 4.7, True, False, 1, 0}
print(thisSet)
print(len(thisSet))

# Access Items
# You cannot access items in a set by referring to an index or a key.
# You can loop through the set items by using a for loop:
for i in thisSet:
    print(i)
print('banana' in thisSet)
print('kiwi' in thisSet)

# Add Set Items
thisSet.add('kolbalish')
print(thisSet)
# Add Any Iterable
newSet={1,2,3,4,5}
thisSet.update(newSet)
print(thisSet)
thisTuple=('abc', 'def')
thisSet.update(thisTuple)
print(thisSet)

# Remove Set Items
# If the item to remove does not exist, remove() will raise an error.
thisSet.remove('banana')
print(thisSet)
# If the item to remove does not exist, discard() will NOT raise an error.
thisSet.discard('abc')
print(thisSet)
# Remove a random item by using the pop() method:
item=thisSet.pop()
print(item)
print(thisSet)
# The clear() method empties the set:
thisSet.clear()
print(thisSet)