T = int(input())


for test_case in range(1, T + 1):
    n, p = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    max_v = 0
    for i in range(n):
        for j in range(n):
            result = matrix[i][j]
            for k in range(1, p + 1):
                if i - k >= 0:
                    result += matrix[i - k][j]
                if i + k < n:
                    result += matrix[i + k][j]
                if j - k >= 0:
                    result += matrix[i][j - k]
                if j + k < n:
                    result += matrix[i][j + k]

            max_v = max(max_v, result)

    print(f"#{test_case} {max_v}")
