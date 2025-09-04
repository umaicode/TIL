'''
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
        used[i] = 0

dfs(4)
'''

MAP = [
    [0, 2, 6, 3, 0, 0],
    [2, 0, 7, 4, 0, 0],
    [6, 7, 0, 0, 0, 0],
    [3, 4, 2, 0, 0, 0],
    [0, 0, 1, 0, 0, 7],
    [0, 0, 0, 0, 0, 0],
]

used = [0] * 6
used[4] = 1 # 시작 노드 방문 처리

def dfs(now):
    print(now, end = ' ')
    for i in range(6):
        if MAP[now][i] == 0: continue
        if used[i] == 1: continue
        # 모든 노드 1회씩 방문
        used[i] = 1 # 방문기록
        dfs(i)
        used[i] = 0 # 모든 경로 : 노드를 다시 방문해야 하니까 (백트래킹)

dfs(4)
