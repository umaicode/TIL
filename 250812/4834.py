t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    numbers = list(map(int, input()))
    numbers.sort()

    dat = [0] * 10
    for num in numbers:
        dat[num] += 1

    max_i = numbers[-1]
    max_v = dat[numbers[-1]]

    for idx, value in enumerate(dat):
        if dat[idx] >= dat[max_i]:
            max_i = idx
            max_v = dat[max_i]

    print(f"#{tc} {max_i} {max_v}")
