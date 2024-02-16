a = int(input("Enter a:"))
b = int(input("Enter b:"))

try:
    result = a / b
except ZeroDivisionError:
    result = None
    print("Error: Can not divide by zero")
finally:
    print("Divison operation completed:", result)