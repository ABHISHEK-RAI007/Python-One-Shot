fruits = ["apple", "mango", "banana", "cherry"] 
# print(fruits)

# checking type of list
# print(type(fruits)) 

# checking length of list
# print(len(fruits))

# checking if an item is present in the list
# if "banana" in fruits:
#     print("Banana is part of the list")

# if "kiwi" not in fruits:
#     print("Kiwi is not part of the list")

#     fruits = ["apple", "mango", "cherry", "banana",] 

#  indexing in list 
# print(fruits[1])
# print(fruits[-3])

# print(fruits[1:3])
# print(fruits[-3:-1])

#  adding elements to a list
# fruits.append("kiwi")
print(fruits)

# fruits.insert(2, "kiwi")
# print(fruits)

# more_fruits = ["kiwi", "papaya"]
# fruits.extend(more_fruits)
# print(fruits)

#  removing elements from the list
# fruits.remove("banana")
# print(fruits)

# fruits.pop(1)
# print(fruits)

# fruits.pop()
# print(fruits)


#  changing/updating item in a list

# fruits[1] =  "kiwi"
# print(fruits)

# fruits[1:3] = ["papaya", ""]
# print(fruits)

# fruits[1:3] = "papaya"
# print(fruits)

#  sorting a list

#  Ascending
# fruits.sort()
# print(fruits)

#  Descending order
# fruits.sort(reverse=True)
# print(fruits)

# fruits.reverse()
# print(fruits)

#  list comprehension
new_fruits = [fruit for fruit in fruits if "a" in fruit]
print(new_fruits)

# #  copy a list
# new_fruits = fruits.copy()
# print(new_fruits)

# new_fruits =  fruits + new_fruits
# print(new_fruits)
