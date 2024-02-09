#  Creating Strings
name1 = "College Wallah"

name2 = "Physics Wallah"

#  Multiline String
name3 = ''' MBA
Wallah '''

print(name1 , name2 , name3)
print(type(name1))
print(type(name2))
print(type(name3))

# Indexing in a string
print(name1[0])
print(name1[-1])

# travarsing a string
#  for loop
for i in name1:
    print(i)

# using list comprehension
list = [char for char in name1]
for i in list:
     print(i)
        
#  Find the length of a string 
print(len(name1))

#  find a char/substring in a string
print(name1.find('o'))
print(name1.find('e'))
print(name1.find('W'))
print(name1.find('z'))

print(name1.find('ege'))
print(name1.find(' '))

#  Slicing of Strings
name1 = "College  Wallah"
# "C o l l e g e   W a l l a h"
#  0 1 2 3 4 5 6 7 8 9 10 11 12 

print(name1[8:])
print(name1[8:11])

#  Negative Indexing
print(name1[-6:])


