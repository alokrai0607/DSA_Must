def isPrime(n):
    if n <= 1:
        print(n, "Is Not Prime")
        return
    
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    
    if count == 2: 
        print(n, "Is Prime")
    else:
        print(n, "Is Not Prime")

isPrime(25)
isPrime(17)
