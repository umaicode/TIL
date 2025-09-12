directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
# TODO
"""
# 1. 열방향 used 배열
used[col] = 1
# 2. / 방향 대각선 used 배열
used[col + row] = 1
# 3. \ 방향 대각선 used 배열
used[col - row + N] = 1
"""
"""
n = int(input())
board = [[0] * n for _ in range(n)]
used = [0] * n
used_left_to_right = [0] * (2 * n)
used_right_to_left = [0] * (2 * n)
result = 0

def queen(row):
    global result
    if row == n:
        result += 1
        return

    for col in range(n):
        # TODO : used 3 conditions check
        # 1. used
        if used[col] == 0 and used_left_to_right[col + row] == 0 and used_right_to_left[col - row + n] == 0:
            used[col] = 1
            used_left_to_right[col + row] = 1
            used_right_to_left[col - row + n] = 1

            queen(row + 1)

            used[col] = 0
            used_left_to_right[col + row] = 0
            used_right_to_left[col - row + n] = 0


queen(0)
print(result)
"""

