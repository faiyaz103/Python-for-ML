# Exponentiation
print(3**2)

# Division
print(9/4)

# Floor Division
print(9//4)

# Logical Operators
x=5
y=6

if x>4 and y<8:
    print("YES")
if x<3 or y==6:
    print("YES")
if not(x==7):
    print("NO")

# Identity Operators
# used to compare the objects, not if they are equal, but if they are 
# actually the same object, with the same memory location:
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is y)
print(x is z)
print(x==y)