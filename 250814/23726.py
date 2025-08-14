n = int(input())
path = []
used = [0] * 7


def kfc(lev, start):
    if lev == n:
        print(*path)
        return

    for i in range(start + 1, 7):
        path.append(i)
        kfc(lev + 1, i - 1)
        path.pop()

kfc(0, 0)
