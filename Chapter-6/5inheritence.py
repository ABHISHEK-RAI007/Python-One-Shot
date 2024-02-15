#  Inheritence
class Parent:
    def __init__(self):
        self.super_attribute = True
        print("This is the parent class")

class Child(Parent):
    def __init__(self):
        print("This is a child class")

child1 = Child()
