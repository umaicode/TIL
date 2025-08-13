t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    target = list(map(int, input().split()))
    matrix = [0] * n

    while matrix == target:
        if target[0] == 1:
            cnt += 1
            for i in range(n):
                matrix[i] = 1

        if target[1] == 1:
            cnt += 1
            for i in range(1, n, 2):
                matrix[i] = 1

        if target[2] == 1:
            cnt += 1
            for i in range(2, n, 3):
                matrix[i] = 1
