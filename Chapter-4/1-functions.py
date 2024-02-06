n = int(input("Enter n:"))

sum = 0
for i in range(1 , n+1):
    sum += i

print("Sum of all numbers til n is", sum)

n1 = int(input("Enter another n:"))
sum1 = 0
for i in range(1 , n1+1):
    sum += i

print("Sum of all numbers til n is", sum1)

#  writng a function for calcuting sum from 1 to n
def sumOneToN(n2):
    sum = 0
    for i in range (1, n2+1):
        sum += i
    return sum

n2 = int(input("Enter n2:"))
#  call function 
output = sumOneToN(n2)
print("Sum of all numbers til n2 is", output)

n3 = int(input("Enter 3:"))
#  call function 
output = sumOneToN(n3)
print("Sum of all numbers til n3 is", output)
