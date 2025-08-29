"""
lst = [4, 5, 1, 1, 5, 4, -3, -13, 9, 20, 13]

idx = int(input())

sum = 0


def get_sum(idx):
    sum = 0
    for i in range(idx, idx + 5):
        sum += lst[i]

    return sum


print(get_sum(idx))
"""

arr = [4, 5, 1, 1, 5, 4, -3, -13, 9, 20, 13]
idx = int(input())


def get_sum(idx):
    sum_v = 0
    # 5개의 합
    for i in range(5):
        sum_v += arr[idx + i]

    return sum_v


print(get_sum(idx))
