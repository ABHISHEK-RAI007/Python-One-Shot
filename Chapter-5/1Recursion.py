# 8:00:06 - 8:49:15: Chapter 5:  Recursion

# Recursion
def factorial(n):

    #  base case
    if n == 0:
        return 1
    
    # recursive case
    ans = n*factorial(n-1)
    return ans

n = int(input("Enter n:"))
print(factorial(n))


















