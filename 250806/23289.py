matrix = [[1, 2, 1, 3, 1], [2, 2, 2, 2, 2], [1, 0, 1, 0, 1], [3, 1, 2, 1, 3]]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

sum_v = 0

for i in range(4):
    sum_v += matrix[1 + dx[i]][2 + dy[i]]

print(sum_v)
