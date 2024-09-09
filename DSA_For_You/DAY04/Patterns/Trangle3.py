def chTrangle(n):
    ch = ord("A")
    for i in range(1,n+1):
        ch += 1
        for j in range(i):
            print(chr(ch-1),end=" ")
        print()


chTrangle(8)

