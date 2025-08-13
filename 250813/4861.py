t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())

    matrix = [list(input()) for _ in range(n)]

    results = []

    for i in range(n):
        for j in range(n - m + 1):
            str1 = ""
            for k in range(m):
                str1 += matrix[i][j + k]
            results.append(str1)

    for j in range(n):
        for i in range(n - m + 1):
            str2 = ""
            for k in range(m):
                str2 += matrix[i + k][j]
            results.append(str2)

    # print(results)
    for result in results:
        if len(result) == m and result == result[::-1]:
            answer = result
            break

    print(f"#{tc} {answer}")
