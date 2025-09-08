import heapq
from collections import defaultdict


def dijkstra(start_node, end_node, cur_tax):
    distances = [float("inf")] * (n + 1)
    pq = []
    heapq.heappush(pq, (0, start_node))
    distances[start_node] = 0

    while pq:
        cur_dist, cur_v = heapq.heappop(pq)

        if cur_dist > distances[cur_v]:
            continue

        for nxt_dist, nxt_v in edges[cur_v]:
            total_dist = cur_dist + nxt_dist + cur_tax
            if total_dist < distances[nxt_v]:
                distances[nxt_v] = total_dist
                heapq.heappush(pq, (total_dist, nxt_v))

    return distances[end_node]


n, m, k = map(int, input().split())

A, B = map(int, input().split())
edges = defaultdict(list)
interest = 0

for _ in range(m):
    start, end, dist = map(int, input().split())
    edges[start].append((dist, end))
    edges[end].append((dist, start))

print(dijkstra(A, B, 0))

for _ in range(k):
    tax = int(input())
    interest += tax
    print(dijkstra(A, B, interest))
