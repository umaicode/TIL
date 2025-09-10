"""
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
"""

def dfs(lev, sum_v):
    global min_v

    if lev == N - 1: # lev은 N-1
        # 마지막 구역에서 사무실로 돌아오는 비용
        sum_v += arr[path[N-1]][0] #
        min_v = min(min_v, sum_v) # 최소값 갱신
        return

    for i in range(1, N): # branch N-1
        if used[i] == 1: continue
        used[i] = 1
        path.append(i)
        dfs(lev + 1, sum_v + arr[path[lev]][i])
        path.pop()
        used[i] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    path = [0] # 사무실 (0)에서 시작
    used = [0] * N
    used[0] = 1 # 사무실 방문처리
    min_v = float('inf')
    dfs(0, 0)
    print(f'#{tc} {min_v}')