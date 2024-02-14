# 9:55:50 - 11:36:04: Chapter 7: Python's OOPS 
class Student:
    
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

student1 = Student()
student1.setName("Shehnaaz")
print(student1.name)
print(student1.getName())

student2 = Student()
student2.setName("Parag")
print(student2.getName())


