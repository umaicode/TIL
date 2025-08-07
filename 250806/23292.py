a, b = map(int, input().split())

matrix = [[1, 2, 1, 3, 1], [2, 2, 2, 2, 2], [1, 0, 1, 0, 1], [3, 1, 2, 1, 3]]

dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]

mul_v = matrix[a][b]

for i in range(4):
    if 0 <= a + dx[i] < 4 and 0 <= b + dy[i] < 4:
        mul_v *= matrix[a + dx[i]][b + dy[i]]
    else:
        mul_v *= 1


print(mul_v)
