# 9:55:50 - 11:36:04: Chapter 7: Python's OOPS 
class Student:
    
    def setName(self, name):
        self.name = name # Class Attributes 

    def getName(self):
        return self.name

student1 = Student()
student1.setName("Shehnaaz")
print(student1.name)
print(student1.getName())

# instance attribute
student1.eng_marks = 45  
print(student1.eng_marks)

student2 = Student()
student2.setName("Parag")
print(student2.getName())


