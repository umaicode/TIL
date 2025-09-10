# import sys
# sys.stdin = open("input.txt", "r")

t = int(input())


def candy_sequence(n1, n2, n3):
    eat_A = 0
    eat_B = 0
    # TODO : 이미 만족한 경우 return 0
    if n1 < n2 < n3:
        return 0

    # TODO : 사탕을 먹고 조건에 만족하면 eat_A + eat_B
    if n2 >= n3:
        while True:
            if n3 > n2 or n2 == 1:
                break
            eat_B += 1
            n2 -= 1

    if n1 >= n2:
        while True:
            if n2 > n1 or n1 == 1:
                break
            eat_A += 1
            n1 -= 1

    # TODO : 조건에 만족하지 않으면 return -1
    if not (n1 < n2 < n3):
        return -1

    return eat_A + eat_B


for tc in range(1, t + 1):
    A, B, C = map(int, input().split())
    print(f"#{tc} {candy_sequence(A, B, C)}")


'''
def get_eating(A, B, C):
    # 1. 이미 만족 하는 경우
    if A < B < C:
        return 0

    # 사탕 개수 계산
    # 예를 들어 B = 5, C = 5 5 - (5 - 1) | B - (C - 1)  1개 먹어야한다.
    # B = 6, C = 5 인 경우 6 - (5 - 1) | B - (C - 1), 2개 먹어야한다.

    eat_B = max(0, B - C + 1)
    new_B = B - eat_B

    eat_A = max(0, A - new_B + 1)
    new_A = A - eat_A

    # 2. 조건 만족하는지 확인 if - else
    if 0 < new_A < new_B < C:
        return eat_A + eat_B
    else:  # 3. 조건을 만족하지 않는 경우
        return -1


T = int(input())
for tc in range(1, T + 1):
    A, B, C = map(int, input().split())
    result = get_eating(A, B, C)
    print(f"#{tc} {result}")
'''