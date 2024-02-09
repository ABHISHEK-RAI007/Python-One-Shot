# Modyfing Strings
#  for converting characters to uppercase
str1 = "New York"
str2 = str1.upper()
print(str2)

#  for converting characters to lowercase
str3 = str2.lower()
print(str3)

#  For capitalising the first character of my string 
str4 = str3.capitalize()
print(str4)

#  for stripping/removing white spaces from the beginning and end of a string characters
str1 = "    Hello World!  "
print(str1.strip())
print(str1)

#  Replace substring
str1 = "Hello World, what a beutiful world this is "
print(str1.replace("World", "Earth"))
print(str1.replace("World", "Earth", 1))

#  Splitting string
str1 = "Ria Pia Sia Tia Mia"
list = str1.split()
print(list)

str1 = "Ria, Pia, Sia, Tia, Mia"
list = str1.split(",", 2)

#  Concatenation of strings
str1 = "Hello World!"
str2 = "what a beutiful world this is"
print(str1 + " " + str2)

#  String Formatting 
student_name  = "Pallavi"
student_marks  = 98

str1 = "The student name is {s} and marks is {m}". format(s = student_name, m = student_marks)
print(str1)


text = "The unexpected always happens "
print(text)
print(len(text))
print(text.find("pp"))
print(text[:11])
print(text.replace('always', 'never'))
text2 = "no matter whats"
new_text = text + text2
print(new_text)


