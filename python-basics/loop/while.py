i=1
while 1<6:
    print(i)
    if i==3:
        break 
    i+=1

# With the else statement we can run a block of code once when the condition no longer is true:

j=0
while j<=5:
    j+=1
    if j==4:
        continue
    print(j)
else:
    print("j is greater than 5")