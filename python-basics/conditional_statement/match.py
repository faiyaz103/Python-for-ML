option=4

match option:
    case 1:
        print("Case 1")
    case 2:
        print('Case 2')
    case 3:
        print("Case 3")
    case _:
        print("This is default if no case matches")

# combine values & If Statements as Guards
# You can add if statements in the case evaluation as an extra condition-check:
day=3
month=4

match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("Workday")
    case 6 | 7 if month==4:
        print("Weekend")
    case _:
        print("No Match Found")