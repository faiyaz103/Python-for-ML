cars=['audi','bmw','toyota','honda']

for x in cars:
    if x=='toyota':continue
    print(x)

# The range() Function

# starting from 0 by default, and increments by 1 (by default), and ends 
# at a specified number.
for x in range(5):
    print(x)
else: #The else block will NOT be executed if the loop is stopped by a break statement.
    print("Out of range")
# Using the start parameter:
for x in range(2,6):
    print(x)
# Increment the sequence with 3
for x in range(0,10,3):
    print(x)

# for loops cannot be empty
for x in range(3):
    pass