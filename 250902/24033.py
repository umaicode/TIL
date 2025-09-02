"""
lst = [[] for _ in range(4)]
lst[0] = [4, 2, 5, 1, 1]
lst[1] = [3, 4, 2]
lst[2] = []
lst[3] = [1, 1, 2, 3]

for i in range(4):
    print(lst[i])
"""

m = [[] for _ in range(4)]  # 4행 2차원 배열
m[0] = [4, 2, 5, 1, 1]
m[1] = [3, 4, 2]
m[3] = [1, 1, 2, 3]

for i in m:
    print(i)
