from collections import deque

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    queue = deque(map(int, input().split()))

    for _ in range(m):
        queue.append(queue.popleft())

    result = queue.popleft()

    print(f"#{tc} {result}")

"""
from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = deque(map(int, input().split()))

    for i in range(M):
        # 가장 왼쪽 원소를 제거하고, 이 원소를 다시 덱이 넣는다.
        arr.append(arr.popleft())

    result = arr[0]
    print(f"{tc} {result}")
"""
