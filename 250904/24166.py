MAP = [[0, 2, 6, 3, 0, 0],
       [2, 0, 7, 4, 0, 0],
       [6, 7, 0, 0, 0, 0],
       [3, 4, 2, 0, 0, 0],
       [0, 0, 1, 0, 0, 7],
       [0, 0, 0, 0, 0, 0]]


def dfs(start, end, cost):
    visited[start] = True

    if start == end:
        distances.append(cost)
        visited[start] = False
        return

    for i in range(6):
        if MAP[start][i] == 0:
            continue
        if visited[i]:
            continue
        dfs(i, end, cost + MAP[start][i])

    visited[start] = False

    return distances


visited = [False] * 6
distances = []
start, end = map(int, input().split())
results = dfs(start, end, 0)
print(max(results))
print(min(results))
