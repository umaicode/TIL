import heapq
from collections import deque

lst = [5, 2, 8, 1, 9]

hq = []
result = deque()

for num in lst:
    heapq.heappush(hq, num)

for i in range(len(hq)):
    result.appendleft(heapq.heappop(hq))

result = list(result)
print(result)
