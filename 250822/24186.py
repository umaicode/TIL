from collections import deque

arr = [[] for _ in range(7)]

arr[5] = [3, 1]
arr[3] = [2]
arr[1] = [4]
arr[4] = [0, 6]


def bfs(arr, start):
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()
        print(now, end=" ")

        for next in range(len(arr[now])):
            q.append(arr[now][next])


bfs(arr, 5)
