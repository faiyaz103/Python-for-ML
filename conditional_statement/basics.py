marks=70
grade=3.5

if marks >= 80 and grade >= 3.5:
    print("A")
elif marks >= 70:
    print("B")
else:
    print("Take Again")

# if statements cannot be empty, but if you for some reason have an if s
# tatement with no content, put in the pass statement to avoid getting an 
# error.
if True:
    pass