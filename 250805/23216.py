ls = [[0] * 4 for _ in range(4)]

ls[0][0] = 7
ls[1][3] = 1
ls[2][1] = 3
ls[3][3] = 9

for i in range(4):
    print(*ls[i])
