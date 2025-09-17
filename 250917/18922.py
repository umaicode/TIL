from heapq import heappush, heappop

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dijkstra():
    pq = []
    distances = [[INF] * M for _ in range(N)]
    distances[0][0] = arr[0][0]
    heappush(pq, (arr[0][0], 0, 0))

    while pq:
        dist, cur_y, cur_x = heappop(pq)

        if cur_y == N - 1 and cur_x == M - 1:
            return dist

        if dist > distances[cur_y][cur_x]:
            continue

        for dy, dx in directions:
            ny = cur_y + dy
            nx = cur_x + dx

            if ny < 0 or nx < 0 or ny >= N or nx >= M:
                continue

            next_dist = dist + arr[ny][nx]
            if next_dist < distances[ny][nx]:
                distances[ny][nx] = next_dist
                heappush(pq, (next_dist, ny, nx))



N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
INF = float("inf")
result = dijkstra()
print(result)