def dfs(start, level):
    visited = [False] * 6
    cur_v = start
    visited[start] = True
    results = []

    if level == 1:
        return

    for i in range(len(adj[cur_v])):
        if adj[cur_v][i] == 1:
            results.append(i)
            dfs(i, level + 1)

    return results


n = int(input())

adj = [[0, 1, 1, 1, 0, 0],
       [0, 0, 0, 0, 1, 1],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0]]
tree_values = "ABTQVX"
result = dfs(n, 0)
# print(result)
for num in result:
    print(tree_values[num])
