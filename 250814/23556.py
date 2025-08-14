n = int(input())
path = []
cnt = 0

# 매개변수로 sum_v
def kfc(level, sum_v):   # 재귀 호출 될 때마다 합계가 누적
    # cnt = 0           # 재귀 호출 할 때마다 0으로 초기화
    global cnt

    # 가지치기
    if sum_v > 10:
        return


    if level == n:
        # if sum_v = 10:  cnt += 1 # 비효율적
        # 모든 경로를 다 탐색해서 느리다.
        cnt += 1
        return

    for i in range(1, 7):
        path.append(i)
        kfc(level + 1, sum_v + i)
        path.pop()


kfc(0, 0)   # level, sum_v

print(cnt)