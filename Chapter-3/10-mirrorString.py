input_string = input("Enter String: ")
n= int(input("Enter n: "))

#  creating dictionary for mirror operation
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
reverse_alaphabets = alphabets[::-1]
dict1 = dict(zip(alphabets, reverse_alaphabets))

#  finding the part of the string on which we will do mirror operation
prefix = input_string[0:n-1]
suffix = input_string[n-1: ]

#  finding the mirror string 
mirror = ""
for i in range(0, len(suffix)):
    mirror = mirror + dict1[suffix[i]]

#  creating the mirror string 
    res = prefix + mirror
    print("The result is:", res)
    

