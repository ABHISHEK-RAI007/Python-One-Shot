#  Write  a function that prints hello world

def printHello():
    # body of my function
    print("Hello World!!")

printHello()

# functions which takes 2 numbers as input returns their sum
def add(n1, n2=0):
    print("n1", n1)
    print("n2", n2)
    sum = n1 + n2
    return sum

x= 2
y = 3
print("The sum is", add(x, y))

#  positional arguments
print("The sum is", add(4, 5))

#  keyword arguments = named arguments
print("The sum is", add(n1 =33, n2 =44))
print("The sum is", add(n2 = 44, n1 = 33))

#  default arguments
def add1(n1, n2=0):
    print("n1", n1)
    print("n2", n2)
    sum1 = n1 + n2
    return sum1
print("The sum1 is", add1(44))

# Arbitrary arguments 
def addAllNumbers(* args):
    sum  = 0
    for i in args:
        sum += i
    return sum
output = addAllNumbers(2,3,5)
print("The sum is", output)

def arbitrary_positional_args(*args):
    for arg in args:
        print(arg)
arbitrary_positional_args(1, 2, 3, "four")

# keyworded arguments 
def  studentInfo(**kwargs):
    for (x,y) in kwargs.items():
        print(x, "is", y)

studentInfo(name="John", age=20, city="New York")
studentInfo(name="Ria", age=22, city="Dehli")



