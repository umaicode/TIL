"""
a = [5, 7, 5, 4, 2, 9]
b = [5, 4, 2, 5, 6]


def is_exist():
    result = []
    for num in a:
        if num in b:
            result.append("O")
        else:
            result.append("X")

    return result


print(*is_exist())
"""

A = [5, 7, 5, 4, 2, 9]
B = [5, 4, 2, 5, 6]


def is_exist(n):  # 존재하면 1, 아니면 0 return
    for i in range(5):
        if B[i] == n:
            return 1

    return 0


for i in range(6):
    if is_exist(A[i]):
        print("O", end=" ")
    else:
        print("X", end=" ")
