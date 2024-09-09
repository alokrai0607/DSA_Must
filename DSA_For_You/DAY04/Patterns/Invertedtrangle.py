n = 4

for i in range(0, n, 1):
    for j in range(0, i, 1):
        print(" ", end=" ")

    for j in range(0, n - i, 1):
        print(i + 1, end=" ")
    print()


'''
1 1 1 1 
  2 2 2 
    3 3 
      4 
'''