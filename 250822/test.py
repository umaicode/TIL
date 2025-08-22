# 이진트리의 DFS 탐색
# 전위순회 (현재노드 -> 왼쪽자식노드 -> 오른쪽자식노드)

bt = [0, "A", "B", "T", "R", "S", "V"]
bt += [0] * 100


def dfs(now):  # now는 현재노드
    # 전위순회를 하다가
    # 왼쪽자식으로 갔는데 8이다. 8번인덱스에는 노드가 없다. - return
    # 오른쪽자식으로 갔는데 9이다. 9번 인덱스에는 노드가 없다. - return
    # 13이야 잘못들어갔어 return
    if bt[now] == 0:
        return

    # print(bt[now])# 현재 노드 먼저 방문
    dfs(now * 2)  # 왼쪽 자식 노드 방문
    dfs(now * 2 + 1)  # 오른쪽 자식 노드 방문


dfs(1)

# 중위순회 (왼쪽 자식 노드 -> 현재 노드 -> 오른쪽 자식 노드)

bt = [0, "A", "B", "T", "R", "S", "V"]
bt += [0] * 100


def dfs(now):  # now는 현재노드
    if bt[now] == 0:
        return

    # dfs(now * 2)  # 왼쪽 자식 노드 방문
    print(bt[now])  # 현재 노드 먼저 방문
    dfs(now * 2 + 1)  # 오른쪽 자식 노드 방문


dfs(1)


# 후위순회 (왼쪽 자식 노드 -> 오른쪽 자식 노드 -> 현재 노드)

bt = [0, "A", "B", "T", "R", "S", "V"]
bt += [0] * 100


def dfs(now):  # now는 현재노드
    if bt[now] == 0:
        return

    dfs(now * 2)  # 왼쪽 자식 노드 방문
    dfs(now * 2 + 1)  # 오른쪽 자식 노드 방문
    print(bt[now])  # 현재 노드 먼저 방문


dfs(1)


bt = [0] * 100

bt[1] = 9  # 루트 노드
bt[2] = 4  # 9의 왼쪽 자식 노드
bt[3] = 12  # 9의 오른쪽 자식 노드
bt[4] = 3
bt[5] = 6
bt[7] = 15
bt[14] = 13
bt[15] = 17


def dfs(now):
    if bt[now] == 0:
        return

    print(bt[now], end=" ")  # 현재노드 방문
    dfs(now * 2)
    dfs(now * 2 + 1)


dfs(1)
