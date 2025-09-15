def make(n):
    parents = [i for i in range(n + 1)]
    ranks = [0] * (n + 1)
    return parents, ranks


def find(x):
    if x == parents[x]:
        return x

    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    rep_x = find(x)
    rep_y = find(y)

    if ranks[rep_x] < ranks[rep_y]:
        parents[rep_x] = rep_y
    elif ranks[rep_x] > ranks[rep_y]:
        parents[rep_y] = rep_x
    else:
        parents[rep_y] = rep_x
        ranks[rep_x] += 1

n = 9
parents, ranks = make(n)
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    union(a, b)
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print("O")
    else:
        print("X")

