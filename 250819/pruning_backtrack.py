def f(i, N, s):  # bit[i]를 결정하는 함수, i-1 원소까지 결정된 부분집합의 합
    global cnt
    global fcnt

    fcnt += 1

    if s == key:  # 부분집합의 합이 찾는 값인 경우
        cnt += 1
    elif s > key:
        return
    elif i == N:  # 더이상 남은 원소가 없는 경우
        return
        # s = 0
        # for i in range(N):
        #     if bit[i]:
        #         s += A[i]
        # if s == key:    # 부분집합의 합이 key인 경우
        #     cnt += 1
    else:
        bit[i] = 1  # A[i] 포함
        f(i + 1, N, s + A[i])
        bit[i] = 0  # A[i] 미포함
        f(i + 1, N, s)


# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = 10
A = [i for i in range(1, N + 1)]  # 1부터 N까지를 원소로 갖는 집합 A

key = 10
bit = [0] * N
cnt = 0  # 합이 key인 경우의 수
fcnt = 0
f(0, N, 0)
print(cnt, fcnt)

"""
1, 2097151
"""
