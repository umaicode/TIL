import heapq

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def supply(start):
    pq = []
    distances = [[float("inf")] * N for _ in range(N)]
    heapq.heappush(pq, (0, 0, 0))
    distances[start][start] = 0

    while pq:
        cur_dist, cur_y, cur_x = heapq.heappop(pq)

        if cur_y == N - 1 and cur_x == N - 1:
            return cur_dist

        if cur_dist > distances[cur_y][cur_x]:
            continue

        for dy, dx in directions:
            ny = cur_y + dy
            nx = cur_x + dx

            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue

            next_dist = cur_dist + arr[ny][nx]
            if next_dist < distances[ny][nx]:
                distances[ny][nx] = next_dist
                heapq.heappush(pq, (next_dist, ny, nx))


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    result = supply(0)
    print(f"#{tc} {result}")
