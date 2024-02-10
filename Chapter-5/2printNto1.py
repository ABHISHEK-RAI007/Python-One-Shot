# 8:00:06 - 8:49:15: Chapter 5:  Recursion
def print_n_to_1(n):

    #  base case
    if n==0:
        return
    
    print(n)
    # recursive case
    print_n_to_1(n-1)

print_n_to_1(7)




















