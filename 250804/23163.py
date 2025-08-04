a, b = map(int, input().split())

if a <= b:
    for i in range(a, b + 1):
        print(i, end=" ")
else:
    for j in range(a, b - 1, -1):
        print(j, end=" ")
