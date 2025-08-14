arr = ["A", "B", "C", "D", "E"]
path = []
n = 3


def kfc(lev, start):
    if lev == n:
        print(*path)
        return

    for i in range(start, 5):
        path.append(arr[i])
        kfc(lev + 1, i + 1)
        path.pop()


kfc(0, 0)
