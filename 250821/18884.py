"""
import heapq

n = int(input())

scores = [500]

cnt = 0

for _ in range(n):
    score1, score2 = map(int, input().split())
    heapq.heappush(scores, score1)
    heapq.heappush(scores, score2)
    k = len(scores)
    result = []
    cnt = 0

    for i in range(k):
        temp = heapq.heappop(scores)
        result.append(temp)
        if i == k // 2:
            print(temp)
    for s in result:
        heapq.heappush(scores, s)
"""

n = int(input())

scores = [500]  # 초기값 500

for _ in range(n):
    a, b = map(int, input().split())
    scores.append(a)
    scores.append(b)
    scores.sort()

    length = len(scores)
    mid = scores[length // 2]
    print(mid)
