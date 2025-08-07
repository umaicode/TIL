y1, x1 = map(int, input().split())
y2, x2 = map(int, input().split())

matrix = [["_"] * 5 for _ in range(4)]

# 상 하 좌 우
dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, -1, 1]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

for dy, dx in directions:
    if y1 + dy < 0 or y1 + dy > 3 or x1 + dx < 0 or x1 + dx > 4:
        continue

    else:
        matrix[y1 + dy][x1 + dx] = "#"


for dy, dx in directions:
    if y2 + dy < 0 or y2 + dy > 3 or x2 + dx < 0 or x2 + dx > 4:
        continue

    else:
        matrix[y2 + dy][x2 + dx] = "#"


for row in matrix:
    print(*matrix)
