ground = [[4, 5, 7, 6], [1, 5, 5, 4], [1, 1, 1, 1]]
peoples = [[5, 6, 4], [1, 5, 3]]
ddang = [[0] * 3 for _ in range(2)]

dat = [0] * 8

for i in range(3):
    for j in range(4):
        dat[ground[i][j]] += 1


for i in range(2):
    for j in range(3):
        ddang[i][j] = dat[peoples[i][j]]

for row in ddang:
    print(*row)
