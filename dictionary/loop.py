car={
    'brand':'ford',
    'model':'mustang',
    'year':2004,
    'origin':'america'
}

# Print all key names in the dictionary, one by one:
for i in car:
    print(i+": "+str(car[i]))

# You can also use the values() method to return values of a dictionary:
for i in car.values():
    print(i)
# You can use the keys() method to return the keys of a dictionary:
for i in car.keys():
    print(i)

# Loop through both keys and values, by using the items() method:
for k,i in car.items():
    print(k, i)