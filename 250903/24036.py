n = int(input())


def dfs(start, level):
    visited = [False] * 5
    cur_v = start
    visited[cur_v] = True
    results = []

    if level == 1:
        return

    for nxt_v in adj[cur_v]:
        if not visited[nxt_v]:
            results.append(nxt_v)
            dfs(nxt_v, level + 1)

    return results


adj = [[] for _ in range(5)]
adj[0] = [1, 3, 4]
adj[1] = [2, 3]
adj[2] = []
adj[3] = [2, 4]
adj[4] = [1, 3]

node_values = "DUSRK"

result = dfs(n, 0)

for num in result:
    print(node_values[num])
