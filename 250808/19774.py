T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    matrix = [list(input()) for _ in range(n)]
    strings_r = []
    strings_c = []
    result = []

    for i in range(n):
        for j in range(n - m + 1):
            string_c = ""
            for k in range(m):
                string_c += matrix[i][j + k]
            result.append(string_c)

    for i in range(n - m + 1):
        for j in range(n):
            string_r = ""
            for k in range(m):
                string_r += matrix[i + k][j]
            result.append(string_r)

    for text in result:
        if text == text[::-1]:
            answer = text

    print(f"#{test_case} {answer}")
