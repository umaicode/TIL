from itertools import combinations, permutations
import sys

sys.stdin = open("input.txt", "r")


def comb(N):
    results = []
    for comb in combinations(ingredients, N // 2):
        results.append(comb)
    # print(results)

    standard = len(results) // 2
    foods1 = results[:standard]
    foods2 = list(reversed(results[standard:]))

    # print(foods1)
    # print(foods2)

    return foods1, foods2


def make_score(foods1, foods2):
    global min_v
    for temp1, temp2 in zip(foods1, foods2):
        score1 = 0
        for p in permutations(temp1, 2):
            score1 += ingredients_scores[p[0]][p[1]]
        score2 = 0
        for p in permutations(temp2, 2):
            score2 += ingredients_scores[p[0]][p[1]]

        diff = abs(score1 - score2)
        if diff < min_v:
            min_v = diff

    return min_v


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    ingredients_scores = [list(map(int, input().split())) for _ in range(N)]
    ingredients = [i for i in range(N)]
    min_v = float("inf")
    foods1, foods2 = comb(N)
    min_v = make_score(foods1, foods2)

    print(f"#{tc} {min_v}")
