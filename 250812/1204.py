t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    scores = list(map(int, input().split()))
    max_i = 0
    max_v = float("-inf")

    dat = [0] * 101
    for score in scores:
        dat[score] += 1

    for idx, value in enumerate(dat):
        if value >= max_v:
            max_v = value
            max_i = idx

    print(dat)
    print(f"#{tc} {max_i}")
