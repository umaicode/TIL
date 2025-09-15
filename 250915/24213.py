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

    if rep_x == rep_y:
        return True

    if ranks[rep_x] < ranks[rep_y]:
        parents[rep_x] = rep_y
    elif ranks[rep_x] > ranks[rep_y]:
        parents[rep_y] = rep_x
    else:
        parents[rep_y] = rep_x
        ranks[rep_x] += 1

    return False

n = 6

arr = "ABCDE"
parents, ranks = make_set(n)
N = int(input())
results = []
for _ in range(N):
    a, b = input().split()
    int_a = arr.index(a)
    int_b = arr.index(b)
    results.append(union(int_a, int_b))

for result in results:
    if not result:
        print("O")
    else:
        print("X")


