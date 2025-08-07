"""
a = [4, 2, 5, 3, 7, 6]
b = [5, 3, 7]

flag = 0
n = int(input())

for i in range(len(b)):
    if a[i + n] != b[i]:
        flag = 1
        break

if flag:
    print("X")
else:
    print("O")
"""

# flag처리
"""
a = [4, 2, 5, 3, 7, 6]
b = [5, 3, 7]

flag = 1
n = int(input())

for i in range(len(b)):
    if a[i + n] != b[i]:
        flag = 0
        break

if flag:
    print("O")
else:
    print("X")
"""


# is_same() 함수
"""
a = [4, 2, 5, 3, 7, 6]
b = [5, 3, 7]


def is_same(n):
    for i in range(3):
        if a[n + i] != b[i]:
            return 0
    return 1


n = int(input())
result = is_same(n)
if result:
    print("O")
else:
    print("X")
"""
