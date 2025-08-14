path = []
used = [0] * 7
n = int(input())

def KFC(lev):
    if lev == n:    # 주사위 3개 던진다.
        print(*path)
        return

    for i in range(1, 7):
        # 만약 used 배열에 기록이 되어 있으면 재귀호출 하지 않는다.
        # -> 다음 레벨로 탐색하지 않는다.
        if used[i] == 1: continue
        used[i] = 1     # 기록
        path.append(i)
        KFC(lev+1)
        path.pop()
        used[i] = 0     # 지워준다.

KFC(0)