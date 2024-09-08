def sumF(n):
    sum=0
    for i in range(1,n+1,1):
        if(i%3==0):
            sum += i
    return sum

print(sumF(26))
