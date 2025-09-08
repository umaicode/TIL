import heapq

adj = [[(15, 1), (17, 2), (22, 3)],
       [(5, 2)],
       [(2, 4), (6, 3), (8, 5)],
       [(7, 5)],
       [(1, 5)],
       []]

distances = [float("inf")] * len(adj)


def dijkstra():
    pq = []
    heapq.heappush(pq, (0, 0))
    distances[0] = 0

    while pq:
        cur_dist, cur_node = heapq.heappop(pq)
        if cur_dist > distances[cur_node]:
            continue
        for next_dist, next_node in adj[cur_node]:
            new_dist = cur_dist + next_dist
            if new_dist < distances[next_node]:
                distances[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))

    return distances


print(*dijkstra())
