phones={
    'samsung': {
        'model': 'A35',
        'os': 'android',
        'year': 2018
    },
    'google': {
        'model': 'pixel 9',
        'os': 'android',
        'year': 2025
    },
    'apple': {
        'model': 'iphone 15',
        'os': 'iOS',
        'year': 2024
    }
}

# Or
samsung= {
    'model': 'A35',
    'os': 'android',
    'year': 2018
}
google= {
    'model': 'pixel 9',
    'os': 'android',
    'year': 2025
}
apple= {
    'model': 'iphone 15',
    'os': 'iOS',
    'year': 2024
}

phones={
    'phone1': samsung,
    'phone2': google,
    'phone3': apple
}

# Access Items
print(phones["phone1"]["os"])

# Loop Through Nested Dictionaries
for k,v in phones.items():
    print(k)

    for i in v:
        print(i+": "+str(v[i]))