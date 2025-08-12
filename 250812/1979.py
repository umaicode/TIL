t = int(input())

for tc in range(1, t + 1):
    n, k = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    result = 0
    # TODO
    # 행순회
    for i in range(n):
        cnt = 0
        for j in range(n):
            if matrix[i][j] == 1:
                cnt += 1
            else:
                if cnt == k:
                    result += 1
                cnt = 0
        if cnt == k:
            result += 1

    # TODO
    # 열순회
    for j in range(n):
        cnt = 0
        for i in range(n):
            if matrix[i][j] == 1:
                cnt += 1
            else:
                if cnt == k:
                    result += 1
                cnt = 0
        if cnt == k:
            result += 1

    print(f"#{tc} {result}")
