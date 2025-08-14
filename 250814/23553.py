# 카드가 3장    branch : 3
# 2장 뽑는다    level : 2

# 중복 순열
# 재귀 호출 + path 배열(흔적 배열)
path = []


def KFC(lev):
    if lev == 3:
        print(*path)  # 정점 레벨에 도달했을 때 print
        return

    for i in range(1, 7):
        path.append(i)  # 재귀호출 전에 append
        KFC(lev + 1)
        path.pop()  # 함수 종료되고 pop


KFC(0)
