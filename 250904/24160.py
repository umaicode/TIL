'''
def dfs(cur_v, target, cost):
    visited[cur_v] = True

    if cur_v == target:
        costs.append(cost)

    for nxt_v in range(len(adj[cur_v])):
        node_cost, connected = adj[cur_v][nxt_v]
        if connected == 1 and not visited[nxt_v]:
            dfs(nxt_v, target, node_cost + cost)

    visited[cur_v] = False


adj = [[(0, 0), (7, 1), (20, 1), (8, 1)],
       [(0, 0), (0, 0), (5, 1), (0, 0)],
       [(15, 1), (0, 0), (0, 0), (0, 0)],
       [(0, 0), (0, 0), (6, 1), (0, 0)]]

visited = [False] * 4
costs = []

n = int(input())

dfs(0, n, 0)
print(*costs)
'''

n = int(input())
MAP = [
    [0, 7, 20, 8],
    [0, 0, 5, 0],
    [15, 0, 0, 0],
    [0, 0, 6, 0]
]

used = [0] * 4
used[0] = 1  # 시작노드 방문처리


# 모든 경로를 탐색 (used배열을 지워줘야한다)
def dfs(now, sum_v):
    if now == n:  # 목적지에 도착하면
        print(sum_v, end=' ')

    for i in range(4):
        if MAP[now][i] == 0: continue
        if used[i] == 1: continue
        used[i] = 1
        # dfs(i, sum_v + 인접행렬의 좌표)
        dfs(i, sum_v + MAP[now][i])
        used[i] = 0  # 모든 경로 탐색


dfs(0, 0)