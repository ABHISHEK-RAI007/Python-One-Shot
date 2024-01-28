#  creating a tuple
colours = ("red", "yellow", "green")

# creating a tuple with a item
# fruit = ("apple",)
fruit = tuple( ("apple") )
print(fruit)

#  check type of the tuple
print(type(colours))
print(type(fruit))

#  check the length of the tuple
print(len(colours))
print(len(fruit))

#  accessing items in tuples

# Positive Indexing
print(colours[0])
print(colours[1])

# Negative Indexing
print(colours[-1])

# Range Indexing

# Range Positive Indexing
print(colours[1:3])

# Range Negative Indexing
print(colours[-2:])

#  check if an exists in tuple
if "green" in colours:
    print("Green is part of tuple")

#  traverse the tuple
    for i in colours:
        print(i)

#  concatenare 2 tuples
more_colours = ("blue", "brown")
colours = colours + more_colours
print("colours")

#  unpacking a tuple 
colours = ("red", "yellow", "green")
colour1, colour2, colour3 = colours
print(colour1, colour2, colour3)


