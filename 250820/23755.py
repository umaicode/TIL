import heapq

lst = [5, 2, 8, 1, 9, 4]
pq = []
result = []


for num in lst:
    heapq.heappush(pq, (num % 2, num))

for i in range(len(pq)):
    result.append(heapq.heappop(pq)[1])

print(*result)
