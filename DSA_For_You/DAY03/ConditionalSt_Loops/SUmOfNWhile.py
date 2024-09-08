def sumOfN(end):
    container = 0
    start = 1
    while start <= end:
        container += start
        start += 1
    return (f'Print of all Numbers till ',end,"is :",container)

print(sumOfN(5))

#We can use break and continue in this program .