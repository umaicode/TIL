"""
n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

k = int(input())

directions = [(-1, 1), (-1, -1), (1, -1), (1, 1)]

kill = 0
kills = []

for i in range(n):
    for j in range(n):
        for dy, dx in directions:
            for step in range(1, k + 1):
                if (
                    i + dy * step < 0
                    or i + dy * step >= n
                    or j + dx * step < 0
                    or j + dx * step >= n
                ):
                    continue
                else:
                    kill += matrix[i + dy * step][j + dx * step]
        kills.append(kill)
        kill = 0

print(max(kills))
"""

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
K = int(input())


def magic(y, x):
    dy = [-1, 1, -1, 1]
    dx = 1, 1, -1, -1
    sum_v = 0

    for i in range(4):
        for j in range(1, K + 1):
            ny = y + dy[i] * j
            nx = x + dx[i] * j
            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue
            sum_v += arr[ny][nx]

    return sum_v


result = float("-inf")
for y in range(N):
    for x in range(N):
        result = max(result, magic(y, x))

print(result)
