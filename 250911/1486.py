from itertools import combinations
#
# import sys
#
# sys.stdin = open("input.txt", "r")
t = int(input())

for tc in range(1, t + 1):
    n, target = map(int, input().split())
    heights = list(map(int, input().split()))

    min_v = float("inf")

    for i in range(1, n + 1):
        for comb in combinations(heights, i):
            sum_v = sum(comb)
            if sum_v >= target:
                min_v = min(min_v, sum_v - target)

    print(f"#{tc} {min_v}")
