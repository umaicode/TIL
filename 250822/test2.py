# 인접 행렬
"""
MAP = [[0] * 7 for _ in range(7)]
MAP[0][1] = 1
MAP[0][2] = 1
MAP[1][3] = 1
MAP[2][4] = 1
MAP[4][5] = 1
MAP[4][6] = 1
print(MAP)
"""

from collections import deque

# 인접 리스트

alist = list([] for _ in range(7))

alist[0] = [1, 2]
alist[1] = [3]
alist[2] = [4]
alist[4] = [5, 6]

q = deque()
q.append(0)  # start 지점

name = "ABCDEFG"

while q:
    # 1. 큐에서 뺀다 (탐색)
    now = q[0]  # now는 탐색하고잇는 현재노드
    q.popleft()
    print(name[now], end=" ")

    # 2. 다음 갈 곳 예약 걸기(큐 등록)
    for i in range(len(alist[now])):
        next = alist[now][i]  # 다음 탐색 할 곳
        q.append(next)
