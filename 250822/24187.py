from collections import deque


def bfs(arr, name):
    q = deque()
    q.append(0)

    while q:
        now = q[0]
        q.popleft()
        print(name[now], end=" ")

        for next in range(len(arr[now])):
            if arr[now][next] == 1:
                q.append(next)


arr = [[0] * 7 for _ in range(7)]
arr[0][1] = 1
arr[0][2] = 1
arr[0][3] = 1
arr[2][4] = 1
arr[3][5] = 1
arr[4][6] = 1

name = "ACBQTPR"


bfs(arr, name)
