ls = [0] * 8

for i in range(8):
    if i < 4:
        ls[i] = 7
    else:
        ls[i] = 15

print(*ls)
