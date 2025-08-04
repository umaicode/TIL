n = int(input())

if n % 2 == 0:
    for i in range(n, n + 12, 2):
        print(i, end=" ")

if n % 2 != 0:
    for j in range(n, n + 33, 3):
        print(j, end=" ")
