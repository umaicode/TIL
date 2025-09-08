import heapq

t = int(input())
directions = [(1, 0), (0, 1)]


def dijkstra(y, x):
    pq = []
    distances[y][x] = arr[y][x]
    heapq.heappush(pq, (distances[y][x], y, x))

    while pq:
        cur_dist, cur_y, cur_x = heapq.heappop(pq)

        if distances[cur_y][cur_x] < cur_dist:
            continue

        if cur_y == n - 1 and cur_x == n - 1:
            return distances[cur_y][cur_x]

        for dy, dx in directions:
            ny = cur_y + dy
            nx = cur_x + dx
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            nxt_dist = cur_dist + arr[ny][nx]
            if nxt_dist < distances[ny][nx]:
                distances[ny][nx] = nxt_dist
                heapq.heappush(pq, (nxt_dist, ny, nx))


for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    distances = [[float("inf")] * n for _ in range(n)]
    result = dijkstra(0, 0)
    print(f"#{tc} {result}")

'''
def dfs(y, x, sum_v):
    global min_sum

    # 좌표 끝에 도달 했을때(정점 노드에 도달 했을때)
    if y == N - 1 and x == N - 1:
        # 최소값 갱신하고 return
        min_sum = min(min_sum, sum_v)
        return

    # 가지치기
    if sum_v >= min_sum:
        return

    # 오른쪽으로 이동
    if x < N - 1:
        dfs(y, x + 1, sum_v + arr[y][x + 1])

    # 아래로 이동
    if y < N - 1:
        dfs(y + 1, x, sum_v + arr[y + 1][x])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = float('inf')
    dfs(0, 0, arr[0][0])
    print(f'#{tc} {min_sum}')

'''