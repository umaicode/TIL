n, m = map(int, input().split())

k = int(input())

matrix = [list(input()) for _ in range(n)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == "@":
            matrix[i][j] = "%"
            for dy, dx in directions:
                for step in range(1, k + 1):
                    if (
                        i + dy * step < 0
                        or i + dy * step >= n
                        or j + dx * step < 0
                        or j + dx * step >= m
                    ):
                        continue
                    else:
                        if matrix[i + dy * step][j + dx * step] == "#":
                            break
                        if matrix[i + dy * step][j + dx * step] == "_":
                            matrix[i + dy * step][j + dx * step] = "%"


for row in matrix:
    print("".join(row))
