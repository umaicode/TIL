import heapq


def is_ugly(n):
    temp = n
    if temp <= 0:
        return False
    if temp == 1:
        return True

    for p in [2, 3, 5]:
        while temp % p == 0:
            temp //= p

    return temp == 1


Q = int(input())
nums = list(map(int, input().split()))

ugly = []
result = []
n = 0

while True:
    n += 1
    if len(ugly) == max(nums):
        break

    if is_ugly(n):
        heapq.heappush(ugly, n)


cnt = 0

while ugly:
    temp = heapq.heappop(ugly)
    cnt += 1
    if cnt in nums:
        result.append(temp)

print(*result)
