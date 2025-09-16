import heapq


def dijkstra(start, end):
    distances = [float("inf")] * len(adj)
    pq = []
    heapq.heappush(pq, (0, start))
    distances[0] = 0

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if cur_cost > distances[cur_node]:
            continue

        if cur_node == end:
            return cur_cost

        for i in range(len(adj[cur_node])):
            if adj[cur_node][i] != 0:
                next_cost = cur_cost + adj[cur_node][i]
                if next_cost < distances[i]:
                    distances[i] = next_cost
                    heapq.heappush(pq, (next_cost, i))


adj = [[0, 5, 10, 7, 0, 12],
       [5, 0, 0, 0, 0, 9],
       [0, 0, 0, 0, 0, 1],
       [0, 0, 2, 0, 1, 0],
       [0, 0, 0, 0, 0, 3],
       [0, 0, 0, 0, 0, 0]]

start, end = input().split()
start = ord(start) - 65
end = ord(end) - 65

result = dijkstra(start, end)
print(result)
