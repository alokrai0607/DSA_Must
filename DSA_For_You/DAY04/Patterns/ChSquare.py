n = 5

for i in range(1, n):
    ch = ord('A')  # Start with ASCII value of 'A'
    for j in range(1, n):
        print(chr(ch), end=" ")
        ch += 1  # Increment to the next character
    print()
