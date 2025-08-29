# lst = [4, 5, 1, 1, 5, 4, -3, -13, 9, 20, 13]
# k = 5

"""
window = sum(lst[:k])
answer = window

for i in range(5, len(lst)):
    window += lst[i] - lst[i - k]
    if window > answer:
        answer = window
        result = i


print(result - k + 1)
"""


"""
window = sum(lst[:k])
max_v = float("-inf")

for i in range(len(lst) - k):
    window += lst[i + k] - lst[i]
    if window >= max_v:
        max_v = window
        max_idx = i + 1

print(max_idx)
"""

arr = [4, 5, 1, 1, 5, 4, -3, -13, 9, 20, 13]

# 처음 윈도우 계산
sum_v = sum(arr[:5])
max_v = sum_v
max_idx = 0

# N-M
for i in range(len(arr) - 5):
    # 1. 다음 윈도우 계산 (현재 i를 기준으로 다음 윈도우를 계산)
    sum_v -= arr[i]  # 첫번째 element 제거
    sum_V += arr[i + 5]  # 마지막 element 추가

    # 2. 최대값 갱신
    if sum_v > max_v:
        max_v = sum_v  # 다음 윈도우의 합
        # 현재 윈도우의 index : i, 다음 윈도우의 index : i + 1
        max_idx = i + 1

print(max_idx)
