import heapq

lst = [(7, "A"), (9, "C"), (7, "C"), (6, "D"), (5, "A")]

pq = []
result = []

for num, ch in lst:
    heapq.heappush(pq, (ch, -num, num))

while pq:
    ch, _, s = heapq.heappop(pq)
    result.append((s, ch))

for temp in result:
    print(f"({temp[0]}, {temp[1]})", end=" ")
