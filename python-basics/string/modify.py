x="   What are you doing hey?   "
print(x.upper())
print(x.lower())

# Remove Whitespace
# Whitespace is the space before and/or after the actual text, and very 
# often you want to remove this space.
print(x.strip())

# The replace() method replaces a string with another string:
# Replaces all occurance
print(x.replace("h", "y"))

# The split() method returns a list where the text between the specified
# separator becomes the list items.
x="What? is? it"
lst=x.split("?")
print(lst, type(lst))

# String Concatenation
text=""
for i in "I am okay":
    text+=(i+" ")
print(text)

# format string
# To specify a string as an f-string, simply put an f in front of the string 
# literal, and add curly brackets {} as placeholders for variables and other
#  operations.
price = 59
txt = f"The price is {price} dollars"
print(txt)
# A modifier is included by adding a colon : followed by a legal formatting 
# type, like .2f which means fixed point number with 2 decimals:
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {price * 3} dollars"
print(txt)