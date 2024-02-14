class Rectangle:

    def set_dimensions(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height* self.width
    
    def perimeter(self):
        return 2*(self.height + self.width)
    
#  creating objects 
rectangle1 = Rectangle()

h = int(input("Enter the height: "))
w = int(input("Enter the width: "))

rectangle1.set_dimensions(h,w)

print("The height and width are:", rectangle1.height, rectangle1.width)
print("The area is: ", rectangle1.area())
print("The perimeter is: ", rectangle1.perimeter())