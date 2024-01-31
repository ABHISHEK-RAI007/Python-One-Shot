phones = {
    "John": 982628,
    "Ria": 468201,
    "Joy": 126830,
}

#  printing the dict
print(phones)

# checking the type of dict
print(type(phones))

# checking the length of dict
print(len(phones))

#  accessing the items in the dict
x = phones["John"]
print(x)
print(phones.get("John"))
print(phones.keys())

#  update value in the dict
print(phones)
phones["John"] = 987677
print(phones)

# add elements in dict
# phones["Kia"] = 234567
# print(phones)

# more_phones = {
#     "Kia" : 234567
# }
# phones.update(more_phones)
# print(phones)

# remove elements in dict
# phones.pop("John")
# print(phones)

# y = phones.popitem()
# print(y)
# print(phones)

# Empty elements in dict
# phones.clear()
# print(phones)

#  printing valus of a dict
for x in phones:
    print(phones[x])
    print(x)
for x in phones.items():
    print(x)
    
for x,y in phones.items():
    print(x,y)
    
#  nested dictionaries
phones = {
    "Area1": {
        "x": 0,
        "y": 1,
        "z": 2
    },
    "Area2": {
        "a": 3,
        "b": 4,
        "c": 5
    },
}
print(phones["Area1"]["y"])
print(phones["Area2"]["c"])