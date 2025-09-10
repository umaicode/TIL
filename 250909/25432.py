from collections import deque

visited = [[0] * 5 for _ in range(5)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def flood_fill(y, x):
    queue = deque()
    queue.append((y, x))
    visited[y][x] = 1

    while queue:
        cur_y, cur_x = queue.popleft()
        for dy, dx in directions:
            ny = cur_y + dy
            nx = cur_x + dx

            if ny < 0 or nx < 0 or ny >= 5 or nx >= 5:
                continue

            if visited[ny][nx] == 0:
                visited[ny][nx] = visited[cur_y][cur_x] + 1
                queue.append((ny, nx))

    return visited


y, x = map(int, input().split())

result = flood_fill(y, x)

for row in result:
    print(*row)
