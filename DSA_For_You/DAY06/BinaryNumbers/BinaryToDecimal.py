def binary_to_decimal(BinaryNum: int):
    answer = 0
    power = 1

    while BinaryNum > 0:
        remainder = BinaryNum % 10
        answer += remainder * power

        BinaryNum //= 10  
        power *= 2  

    return answer

print(binary_to_decimal(101010))