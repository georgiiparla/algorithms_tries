def factorial(n):
    if 0 <= n <= 1:
        return n
    else:
        return n * factorial(n-1)
    

print(factorial(5))
