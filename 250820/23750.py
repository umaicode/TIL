import heapq

lst = [5, 2, 8, 1, 9]

hq = []
result = []

for num in lst:
    heapq.heappush(hq, num)

for i in range(len(hq)):
    result.append(heapq.heappop(hq))

print(result)
