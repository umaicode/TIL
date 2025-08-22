bt = [0] * 100

bt[1] = 9
bt[2] = 4
bt[3] = 12
bt[4] = 3
bt[5] = 6
bt[7] = 15
bt[14] = 13
bt[15] = 17


def dfs(now):
    if bt[now] == 0:
        return

    dfs(now * 2)
    dfs(now * 2 + 1)
    print(bt[now], end=" ")


dfs(1)
