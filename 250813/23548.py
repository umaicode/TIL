"""
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            for l in range(1, 4):
                print(i, j, k, l)
"""


def numbers(n, a=1, b=1, c=1, d=1):
    if a > n:
        return
    if b > n:
        return numbers(n, a + 1, 1, 1, 1)
    if c > n:
        return numbers(n, a, b + 1, 1, 1)
    if d > n:
        return numbers(n, a, b, c + 1, 1)

    print(a, b, c, d)
    numbers(n, a, b, c, d + 1)


numbers(3)
