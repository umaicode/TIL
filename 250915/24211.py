def make_set(n):
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


n = 7
parents, ranks = make_set(n)
union(5, 7)
union(6, 7)
union(1, 2)

a, b = map(int, input().split())
if find(a) == find(b):
    print("O")
else:
    print("X")