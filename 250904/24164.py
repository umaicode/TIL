MAP = [[0, 2, 6, 3, 0, 0],
       [2, 0, 7, 4, 0, 0],
       [6, 7, 0, 0, 0, 0],
       [3, 4, 2, 0, 0, 0],
       [0, 0, 1, 0, 0, 7],
       [0, 0, 0, 0, 0, 0]]

visited = [False] * 6
cnt = 0


def dfs(start, end):
    global cnt

    if start == end:
        cnt += 1
        return

    for i in range(6):
        if MAP[start][i] == 0:
            continue
        if visited[i]:
            continue
        visited[i] = True
        dfs(i, end)
        visited[i] = False

    return cnt


start, end = map(int, input().split())
print(dfs(start, end))
