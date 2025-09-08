def electric_cart(level, cost):
    global min_v

    if cost > min_v:
        return

    if level == n - 1:
        total = cost + arr[path[-1]][0]

        if total < min_v:
            min_v = total
        return

    for i in range(1, n):
        if used[i] == 1:
            continue
        used[i] = 1
        path.append(i)
        electric_cart(level + 1, cost + arr[path[-2]][i])
        path.pop()
        used[i] = 0


t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    min_v = float("inf")

    path = [0]
    used = [0] * n

    electric_cart(0, 0)

    print(f"#{tc} {min_v}")
