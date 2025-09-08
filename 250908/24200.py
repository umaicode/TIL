from collections import deque


def bfs(start, end):
    queue = deque()
    queue.append((0, start))
    visited[start] = True

    while queue:
        cur_cnt, cur_v = queue.popleft()
        if cur_v == end:
            return cur_cnt

        for i in range(len(adj[cur_v])):
            if adj[cur_v][i] == 1 and not visited[i]:
                queue.append((cur_cnt + 1, i))
                visited[i] == True

    return -1


results = []
name = "ABCDE"
adj = [
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
]

visited = [False] * 5

start, end = map(int, input().split())

print(bfs(start, end))
