"""
def recursive(n, a):
    print(a, end=" ")
    if a == n:
        return
    else:
        recursive(n, a + 1)


def recursive2(n, a):
    print(a, end=" ")
    if a == 0:
        return
    else:
        recursive2(n, a - 1)


recursive(5, 0), recursive2(5, 5)
"""


def print_number(n, a):
    if a > 5:
        return
    print(a, end=" ")
    print_number(n, a + 1)
    print(a, end=" ")


print_number(5, 0)


def pnum(n):
    if n < 0:
        return
    print(5 - n)
    pnum(5 - n)
    print(5 - n)


pnum(5)
