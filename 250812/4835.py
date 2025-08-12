t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    sums = []
    for i in range(n - m + 1):
        sum_v = 0
        for step in range(m):
            sum_v += arr[i + step]
        sums.append(sum_v)

    result = max(sums) - min(sums)

    print(f"#{tc} {result}")
