def PosOrNeg(n):
    if(n%2==0):
        return(n,"Is Positive")
    elif(n%2==1):
        return(n,"Is Negative")

print(PosOrNeg(25458578))
print(PosOrNeg(-25458578))
