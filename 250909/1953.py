"""
from collections import deque
# import sys
#
# sys.stdin = open("input.txt", "r")
#

def arrest():
    queue = deque()
    cnt = 1
    queue.append((r, c))
    visited[r][c] = 1

    while queue:
        cur_y, cur_x = queue.popleft()
        cur_pipe = arr[cur_y][cur_x]

        if visited[cur_y][cur_x] == l:
            continue

        for i in range(4):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue

            if visited[ny][nx] == 0 and arr[ny][nx] != 0:
                next_pipe = arr[ny][nx]

                if pipe[cur_pipe][i] and pipe[next_pipe][opp[i]]:
                    visited[ny][nx] = visited[cur_y][cur_x] + 1
                    queue.append((ny, nx))
                    cnt += 1

    return cnt


# 상 하 좌 우
pipe = [[0, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [1, 0, 0, 1],
        [0, 1, 0, 1],
        [0, 1, 1, 0],
        [1, 0, 1, 0]]

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

opp = [1, 0, 3, 2]

t = int(input())

for tc in range(1, t + 1):
    n, m, r, c, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    result = arrest()
    print(f"#{tc} {result}")
"""

from collections import deque

# 자료구조!
# pipe의 모든 경우 [상, 하, 좌, 우] -> 8개의 종류
pipe = [[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 0, 1 ], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0]]
# 델타배열(방향배열) : 상 하 좌 우
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
# 다음칸으로 연결되는 파이프의 방향은 반대방향이어야 한다
# 상, 하, 좌, 우 : 0, 1, 2, 3
# 상 -> 하, 하 -> 상, 좌 -> 우, 우 -> 좌
opp = [1, 0, 3, 2]

def bfs():
    q = deque()
    visited = [[0] * M for _ in range(N)] # NxM행렬
    q.append((R, C)) # 시작 위치 큐에 추가
    visited[R][C] = 1 # 시작 노드 방문 표시
    cnt = 1

    while q:
        # 1. 큐에서 뺀다(탐색)
        y, x = q.popleft()

        # 언제 cnt 반환할까?
        # 시간이 L에 도달하면 cnt 반환
        if visited[y][x] == L:
            return cnt

        # 4방향
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            # 좌표범위안에, 방문하지 않아야하고, 파이프가 연결 되었는지(현재파이프 and 다음파이프)
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and pipe[arr[y][x]][i] and pipe[arr[ny][nx]][opp[i]]:
                # 2. 다음갈곳 예약 걸기
                q.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1 # 방문표시
                cnt += 1

    return cnt # 총 반문한 칸수 반환

T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = bfs()
    print(f'#{tc} {result}')