#  Polymorphism
class Animal:
    def speaks(): #abstract method which will be overwritten 
        # pass
        print("Generic Noise")

class Dog(Animal):
    def speaks(self):
        print("Barks")

class Cat(Animal):
    def speaks(self):
        print("Meow")

class Cow(Animal):
    def speaks(self):
        print("Mooo")

dog = Dog()
cat = Cat()
cow = Cow()

dog.speaks()
cat.speaks()
cow.speaks()




