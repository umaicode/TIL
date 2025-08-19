N = int(input())
path = []


def KFC(lev, start):
    if lev == N:  # N번 던진다 : level == N
        print(*path)
        return

    for i in range(1, 7):  # branch : 최대 6
        path.append(i)
        KFC(lev + 1, i)
        path.pop()


KFC(0, 1)
