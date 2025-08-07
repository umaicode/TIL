matrix = [[1, 2, 1, 3, 1], [2, 2, 2, 2, 2], [1, 0, 1, 0, 1], [3, 1, 2, 1, 3]]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

sum_v = 0

for i in range(4):
    if 0 <= 0 + dx[i] < 4 and 0 <= 1 + dy[i] < 4:
        sum_v += matrix[0 + dx[i]][1 + dy[i]]
    else:
        sum_v += 0


print(sum_v)
