def sumOfOddEven(end):
    start = 1
    OddContainer = 0
    EvenContainer = 0
    while start <= end:
        if start % 2 == 0:
            EvenContainer += start
        elif start % 2 == 1:
            OddContainer += start
        start += 1
    return ("Sum of Even Numbers :",EvenContainer,"Sum of Odd Numbers is :",OddContainer)
    
print(sumOfOddEven(5))


