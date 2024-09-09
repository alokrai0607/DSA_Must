
def printpat(n):
    for i in range(1,n):
        for j in range(i):
            print("*",end=" ")
        print()


printpat(11)