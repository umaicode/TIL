MAP = [[0] * 6 for _ in range(6)]

MAP[0][1] = 2
MAP[1][0] = 2
MAP[0][2] = 6
MAP[2][0] = 6
MAP[0][3] = 3
MAP[3][0] = 3

MAP[1][2] = 7
MAP[2][1] = 7
MAP[1][3] = 4
MAP[3][1] = 4
MAP[3][2] = 2

MAP[4][2] = 1
MAP[4][5] = 7

used = [0] * 6
used[4] = 1 # 시작노드 방문 처리

def dfs(now):
    print(now, end = " ")
    for i in range(6):
        if MAP[now][i] == 0: continue
        # 이미 갔던 곳(방문했던 곳)이라면 무시
        if used[i] == 1: continue
        # 방문표시
        used[i] = 1
        dfs(i)

dfs(4)