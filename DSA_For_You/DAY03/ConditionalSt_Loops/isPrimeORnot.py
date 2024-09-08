def isPrimeOrNot(n):
    if n < 2:
        return "is Less than 2"
    
    count = 0
    for i in range(1,n+1):
        if n%i==0:
            count += 1

    if count == 2 :
        return n,"is Prime"
    else:
        return n,"is not Prime"
    
print(isPrimeOrNot(12))
print(isPrimeOrNot(13))