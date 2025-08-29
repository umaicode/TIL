"""
lst = [4, 5, 1, 1, 5, 4, -3, -13, 9, 20, 13]


def get_sum(lst):
    idx = [0, 1, 2, 3, 4, 5, 6]
    result = []
    sum = 0
    for i in idx:
        for j in range(5):
            sum += lst[i + j]
        result.append((i, sum))
        sum = 0

    result.sort(key=lambda x: x[1])
    ans = result.pop()

    return ans[0]


print(get_sum(lst))
"""

arr = [4, 5, 1, 1, 5, 4, -3, -13, 9, 20, 13]
idx = int(input())


def get_sum(idx):
    sum_v = 0
    # 5개의 합
    for i in range(5):
        sum_v += arr[idx + i]

    return sum_v


N = len(arr)
M = 5

max_v = float("-inf")
for idx in range(N - M + 1):
    ret = get_sum(idx)
    if ret > max_v:  # 최대값 갱신
        max_v = ret
        max_idx = idx  # 최대값 일 때 인덱스

print(get_sum(idx))
