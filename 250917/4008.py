def backtrack(level, sum_v):
    global min_v
    global max_v

    if level == N - 1:
        if min_v > sum_v:
            min_v = sum_v
        if max_v < sum_v:
            max_v = sum_v
        return

    for i in range(4):
        temp = sum_v
        if operators[i] == 0:
            continue
        if i == 0:
            sum_v += numbers[level + 1]
        elif i == 1:
            sum_v -= numbers[level + 1]
        elif i == 2:
            sum_v *= numbers[level + 1]
        else:
            if sum_v < 0:
                sum_v = abs(sum_v) // numbers[level + 1] * (-1)
            else:
                sum_v //= numbers[level + 1]

        operators[i] -= 1
        backtrack(level + 1, sum_v)
        operators[i] += 1
        sum_v = temp


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    operators = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    min_v = float("inf")
    max_v = float("-inf")

    backtrack(0, numbers[0])

    if min_v < 0:
        result = max_v + abs(min_v)
    else:
        result = max_v - min_v

    print(f"#{tc} {result}")
