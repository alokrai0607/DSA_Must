def factorial_fun(n):
    prod = 1
    for i in range(1,n+1):
        prod *= i
    return ("Factorial of",n,"is :",prod)

print(factorial_fun(5))
print(factorial_fun(15))