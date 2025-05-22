# All string methods returns new values. They do not change the original string.

# Quotes Inside Quotes
x="Hello 'who' is this?"
y='what is "he" doing?'
print(x,y)

# Multiline Strings
x="""Loremwefewf efwfefwfwef fewefwfee
weffwfweff fwefwffw
fewfwffweefef
fef eff
ee"""
# Or three single quotes: '''-----'''
print(x)

# Strings are Arrays
y="Hello World"
print(y[3])

for i in y:
    print(i)

# length
print(len(y))

# check if a certain phrase or character is present in a string, we can use the keyword in.
if "llo" in y:
    print("YES")

if "hell" not in y:
    print("Not there")

# Slice
# Specify the start index and the end index, separated by a colon, to return a part of the string.
print(y[3:8])
print(y[:7])
print(y[2:])
# Use negative indexes to start the slice from the end of the string:
print(y[-7:-3])