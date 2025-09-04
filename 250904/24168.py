n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

start, end = map(int, input().split())

max_v = 0
min_v = float("inf")
visited = [False] * n


def dfs(start, cost):
    visited[start] = True
    global max_v
    global min_v

    if start == end:
        max_v = max(max_v, cost)
        min_v = min(min_v, cost)
        visited[start] = False
        return

    for i in range(n):
        if grid[start][i] == 0:
            continue
        if visited[i]:
            continue
        dfs(i, cost + grid[start][i])

    visited[start] = False

    return min_v, max_v


result = dfs(start, 0)
print(result[0])
print(result[1])
