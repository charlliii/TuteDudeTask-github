# Task 1: Calculate Factorial Using a Function
def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n - 1)
ans=fact(5)
print(ans)