'''
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
'''
name = "ABTQVX"

MAP = [[0] * 6 for _ in range(6)]
MAP[0][1] = 1
MAP[0][2] = 1
MAP[0][3] = 1
MAP[1][4] = 1
MAP[1][5] = 1

num = int(input())
for i in range(6):
    if MAP[num][i] == 1: print(name[i])