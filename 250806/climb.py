def magic(y, x, count):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    heights = []
    start = matrix[y][x]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= n or nx >= n:
            continue
        else:
            if matrix[ny][nx] < start:
                heights.append((ny, nx))

    if heights:
        heights.sort(key=lambda x: matrix[x[0]][x[1]])
        ny, nx = heights[-1]
        return magic(ny, nx, count + 1)
    else:
        return count


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    steps = []

    for i in range(n):
        for j in range(n):
            step = magic(i, j, 1)
            steps.append(step)
    print(f"#{test_case} {max(steps)}")
