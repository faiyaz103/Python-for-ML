# The union() method returns a new set with all items from both sets.
set1={'a','b','c'}
set2={1,2,3,4,5}
tuple1=('banana', 'apple')
set3=set1.union(set2, tuple1)
print(set3)

# The intersection() method will return a new set, that only contains the 
# items that are present in both sets.
fruits1={'apple', 'banana', 'mangoes'}
fruits2={'lemon', 'oranges', 'apple'}
fruits=fruits1.intersection(fruits2)
print(fruits)
# The intersection_update() method will also keep ONLY the duplicates, but i
# t will change the original set instead of returning a new set.
fruits1.intersection_update(fruits2)
print(fruits1)

# The difference() method will return a new set that will contain only the 
# items from the first set that are not present in the other set.
fruits1={'apple', 'banana', 'mangoes'}
fruits=fruits1.difference(fruits2)
print(fruits)
# The difference_update() method will also keep the items from the first set 
# that are not in the other set, but it will change the original set instead of returning a new set.

# The symmetric_difference() method will keep only the elements that are NOT 
# present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)
# The symmetric_difference_update() method will also keep all but the 
# duplicates, but it will change the original set instead of returning a new set.