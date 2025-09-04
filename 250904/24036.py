'''
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
'''

# 인접행렬
MAP = [[0] * 5 for _ in range(5)] # 5x5 행렬
MAP[0][1] = 1
MAP[0][3] = 1
MAP[0][4] = 1
MAP[1][2] = 1
MAP[1][3] = 1
MAP[3][2] = 1
MAP[3][4] = 1
MAP[4][1] = 1
MAP[4][3] = 1
# 인접리스트
alist = [[] for _ in range(5)]
alist[0] = [1, 3, 4]
alist[1] = [2, 3]
alist[3] = [2, 4]
alist[4] = [1, 3]


node_name = 'DUSRK'

num = int(input())

for i in range(len(alist[num])):
    # 인접 행렬
    # if MAP[name][i] == 1: print()
    # 인접 리스트
    next = alist[num][i]
    print(node_name[next])

