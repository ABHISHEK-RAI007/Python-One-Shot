# Class Constructor 

class Rectangle:

    def __init__(self, height, width):
        print("A recttangle is created with height: {Height} and width: {width}")
        self.height = height
        self.width = width


    def set_dimensions(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height* self.width
    
    def perimeter(self):
        return 2*(self.height + self.width)
    
#  creating objects 
    
# h = int(input("Enter the height: "))
# w = int(input("Enter the width: "))
    
rectangle1 = Rectangle(4, 5)
rectangle2 = Rectangle(6, 7)
rectangle3 = Rectangle(3, 4)
# rectangle1.set_dimensions(h,w)

# print("The height and width are:", rectangle1.height, rectangle1.width)
# print("The area is: ", rectangle1.area())
# print("The perimeter is: ", rectangle1.perimeter())

