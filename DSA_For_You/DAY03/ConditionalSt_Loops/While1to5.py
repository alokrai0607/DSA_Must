
#Print the even number till N using while loop .
def whileloop(n):
    lis =[]
    i=1
    while i <= n:
        if(i%2==0):
            lis.append(i)
        i += 1
    return lis
        
    
print(whileloop(5))
print(whileloop(25))

