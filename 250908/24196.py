from collections import deque

n = int(input())
name = "ABCDE"
graph = [[1, 2], [0, 2], [0, 1, 3], [2, 4], [3]]
visited = [False] * 5


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        cur_node = queue.popleft()
        print(name[cur_node], end=" ")
        for nxt_node in graph[cur_node]:
            if not visited[nxt_node]:
                visited[nxt_node] = True
                queue.append(nxt_node)


bfs(n)
