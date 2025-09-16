def find_set(x):
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    rep_x = find_set(x)
    rep_y = find_set(y)

    if rep_x == rep_y:
        return

    if rep_x < rep_y:
        parents[rep_y] = rep_x
    else:
        parents[rep_x] = rep_y


N, M = map(int, input().split())
schools = [""] + list(input().split())
# print(schools)
edges = []
for _ in range(M):
    start, end, weight = map(int, input().split())
    if schools[start] != schools[end]:
        edges.append((start, end, weight))

cnt = 0
result = 0
parents = [i for i in range(N + 1)]
edges.sort(key=lambda x: x[2])

for u, v, w in edges:
    if find_set(u) != find_set(v):
        union(u, v)
        cnt += 1
        result += w

    if cnt == N - 1:
        break

if cnt == N - 1:
    print(result)
else:
    print(-1)
