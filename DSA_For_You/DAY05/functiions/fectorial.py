def fectorial(n):
    product = 1
    for i in range(1,n+1):
        product *= i
    return product

print(fectorial(15))