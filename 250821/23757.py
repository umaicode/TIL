import heapq

lst = [(9, "A"), (8, "B"), (9, "A"), (10, "C"), (15, "A")]
pq = []
result = []

n = int(input())

for num, ch in lst:
    heapq.heappush(pq, (num, -ord(ch), ch))

for i in range(n):
    (number, _, s) = heapq.heappop(pq)
    new_number = (number * 2) % 17
    heapq.heappush(pq, (new_number, _, s))

for i in range(len(pq)):
    temp = heapq.heappop(pq)
    print(f"({temp[0]}, {temp[2]})", end=" ")
