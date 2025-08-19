"""
# 25년 1차 IM 기출 문제
# 1번 방부터 있다.
# 5 N
# 1 2 3 4 5 번방
# 0 1 1 2 0 가야하는 방

# (1) -> (2) -> (1) -> (2) -> (3) -> (1) -> (2) -> (3) -> (4) -> (2) -> (3) -> (4) -> (5)

# 구현 : 인덱스를 이용하자 !!!
# 인덱스를 이동할 때마다 counting 하자 !!
# 마지막에 cnt 출력
# for 문보다 while 쓰는게 낫다.
"""

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # 인덱스를 값으로 쓸거, 1번 인덱스부터 사용
    arr = [0] + list(map(int, input().split()))

    cnt = 0

    # 한번 들렸던 곳이면 오른쪽으로 이동
    # 한번 들렸던 곳이면 방문 체크를 0번
    now = 1  # 초기식
    while now < N:  # 조건식
        if arr[now] == 0:
            now += 1  # 증감식(오른쪽 방으로 이동)
        else:
            next_idx = arr[now]  # 다음 갈 곳
            arr[now] = 0
            now = next_idx
        cnt += 1

    print(f"#{tc} {cnt}")


"""
내 풀이
def portal(N, lst):
    cnt = 0

    for i in range(N):
        if i == N - 1:
            break
        if lst[i] == 0:
            cnt += 1
            continue
        else:
            start = lst[i] - 1
            cnt += 1
            for _ in range(start, i + 1):
                cnt += 1

    return cnt


t = int(input())

for tc in range(1, t + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    result = portal(N, lst)

    print(f"#{tc} {result}")


"""
