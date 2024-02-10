# 8:00:06 - 8:49:15: Chapter 5:  Recursion

def sum_1_to_N(n):

    # base case
    if n==1:
        return 1
    
    #  recursive case
    ans = n + sum_1_to_N(n-1)
    return ans

n = int(input("Enter n:"))
print(sum_1_to_N(n))


