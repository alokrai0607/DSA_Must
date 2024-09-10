def digitSum(num):
    digSum=0
    while (num>0):
        last_digit = num % 10
        num //= 10
        digSum += last_digit
    return digSum

print(round(digitSum(12345)))

print(round(digitSum(12345555)))


