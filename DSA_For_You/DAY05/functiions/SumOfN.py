def sumOfN(n):
    total = 0
    for i in range(n+1):
        total += i
    return total

print(sumOfN(5))
print(sumOfN(25))