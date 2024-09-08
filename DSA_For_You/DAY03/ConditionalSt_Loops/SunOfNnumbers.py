def sumOfN(n):
    sum = 0
    for i in range (1,n+1,1):
        sum += i
    return sum

print(sumOfN(5))