arr = []

a, b = map(int, input().split())

for i in range(8):
    if i < 3:
        arr.append(a)
    elif 3 <= i < 5:
        arr.append(b)
    else:
        arr.append(a + b)

print(*arr)
