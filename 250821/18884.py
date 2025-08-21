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

# 시간복잡도 O(N^2logN)
"""
import heapq

max_heap = []  # 내림차순 중간값 보다 작은 값 (최대힙)
min_heap = []  # 오름차순 중간값 보다 큰값 (최소힙)
mid = 500


def push(v):
    if mid > v:  # 중간값보다 작으면 최대 힙에 추가
        heapq.heappush(max_heap, -v)
    else:  # 중간값보다 크거나 같으면 최소 힙에 추가
        heapq.heappush(min_heap, v)


n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    push(a)
    push(b)

    # 경우가 두 가지
    # 1. 왼쪽이 더 많을 경우 (최대 힙의 크기가 더 클 경우)
    # 2. 오른쪽이 더 많을 경우 (최소 힙의 크기가 더 클 경우)
    if len(max_heap) > len(min_heap):
        # 최대 힙이 많으니까 최소 힙에 넣기 (갯수 맞추기)
        heapq.heappush(min_heap, mid)

        # 최대 힙에서 가장 큰 값 꺼내서 새로운 중간값으로 설정
        mid = -heapq.heappop(max_heap)

    elif len(max_heap) < len(min_heap):
        heapq.heappush(max_heap, -mid)
        mid = heapq.heappop(min_heap)

# 시간복잡도 O(NlogN)
