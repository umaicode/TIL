# import sys
#
# sys.stdin = open("input.txt", "r")


def make_set(n):
    parents = [i for i in range(n + 1)]
    ranks = [0] * (n + 1)
    return parents, ranks


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

    if ranks[rep_x] < ranks[rep_y]:
        parents[rep_x] = rep_y
    elif ranks[rep_x] > ranks[rep_y]:
        parents[rep_y] = rep_x
    else:
        parents[rep_y] = rep_x
        ranks[rep_x] += 1


names = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
indians = 26
parents, ranks = make_set(indians)
team_cnt = 0
individuals = 0
teams = [0] * (indians + 1)

n = int(input())
for _ in range(n):
    indian_1, indian_2 = input().split()
    int_indian_1 = names.index(indian_1)
    int_indian_2 = names.index(indian_2)
    union(int_indian_1, int_indian_2)


# for rep_num in parents[1:]:
#     teams[rep_num] += 1

for i in range(1, indians + 1):
    rep = find_set(i)
    teams[rep] += 1
# print(teams)

for i in range(1, len(teams)):
    if teams[i] > 1:
        team_cnt += 1
    elif teams[i] == 1:
        individuals += 1
    else:
        continue

print(team_cnt)
print(individuals)
