def dfs(cur_v):
    path.append(cur_v)

    for nxt_v in range(len(adj[cur_v])):
        if adj[cur_v][nxt_v] == 1 and not visited[adj[cur_v][nxt_v]]:
            dfs(nxt_v)
    return path


adj = [[0, 1, 1, 1, 0, 0],
       [0, 0, 0, 0, 1, 1],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0]]
visited = [False] * 6
path = []

print(*dfs(0))
