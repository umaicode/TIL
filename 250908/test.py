# 중복순열
"""
path = []


def recur(lev):
    if lev == 2:  # level = 2
        print(path)
        return

    for i in range(3):  # branch = 3
        path.append(i)
        recur(lev + 1)
        path.pop()


recur(0)
"""

# 순열
"""
path = []
used = [0] * 3


def recur(lev):
    if lev == 2:    # level : 2
        print(path)
        return

    for i in range(3):  # branch : 3
        if used[i] == 1:
            continue    # 이미 사용한 숫자면 continue
        used[i] = 1
        path.append(i)
        recur(lev + 1)
        path.pop()
        used[i] = 0 # 사용기록 지워주기


recur(0)
"""

# 부분집합
"""
arr = ["A", "B", "C"]
n = len(arr)  # 개수 (n값)


def get_sum(tar):
    for i in range(n):
        if tar & 0x1:
            print(arr[i], end="")
        tar >>= 1


for tar in range(1 << n):
    print("{", end="")
    get_sum(tar)
    print("}")
"""

# 조합
"""
arr = ["A", "B", "C", "D", "E"]

for a in range(5):
    start1 = a + 1
    # a에서 뽑은건 포함하면 안된다.
    for b in range(start1, 5):  # branch가 최대 5
        start2 = b + 1
        # b에서 뽑은건 포함하면 안된다.
        for c in range(start2, 5):  # branch가 최대 5
            print(arr[a], arr[b], arr[c])
"""

# 조합 재귀호출
"""         
arr = ["A", "B", "C", "D", "E"]
path = []
n = 3  # 5명중에 3명을 뽑는다


def recur(lev, start):
    if lev == n:  # level은 n(n명 뽑는다)
        print(*path)
        return

    for i in range(start, 5):  # branch가 최대 5
        path.append(arr[i])
        recur(lev + 1, i + 1)
        path.pop()


recur(0, 0)
"""
