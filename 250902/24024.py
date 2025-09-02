"""
name = "12345"

MAP = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
]

n = int(input())

for i in range(5):
    if MAP[n - 1][i] == 0:
        continue
    print(name[i])
"""

# 인접 행렬

MAP = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
]

num = int(input())  # 노드 값
n = num - 1  # 노드 번호
for i in range(5):
    if MAP[n][i] == 0:
        continue
    print(i + 1)  # 노드 값
