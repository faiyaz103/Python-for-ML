letterList=['toyota','audi', 'Bmw', 'Volvo']
numList=[123,65,3,9,0,34]

# Ascending
letterList.sort()
numList.sort()
print(letterList)
print(numList)

# descending
numList.sort(reverse=True)
print(numList)

# customize your own function by using the keyword argument key = function
def myfunc(num):
    # Sort the list based on how close the number is to 50:
    return abs(num-50)

numList.sort(key=myfunc)
print(numList)

# By default the sort() method is case sensitive, resulting in all capital 
# letters being sorted before lower case letters:
# if you want a case-insensitive sort function, use str.lower as a key function:
letterList.sort(key=str.lower)
print(letterList)

# Reverse Order
letterList.reverse()
print(letterList)