def dectobinary(decNum: int):
    ans = 0
    power = 1

    while decNum > 0:
        rem = decNum % 2
        decNum //= 2  

        ans += (rem * power)
        power *= 10

    return ans

print(dectobinary(25))  
