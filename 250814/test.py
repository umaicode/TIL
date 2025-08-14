# 카드가 3장    branch : 3
# 2장 뽑는다    level : 2

# 중복 순열
# 재귀 호출 + path 배열(흔적 배열) - 스택의 개념

'''
path = []
def KFC(lev):

    if lev == 2:
        print(path)     # 정점 레벨에 도달했을 때 print
        return

    for i in range(3):
        path.append(i)  # 재귀호출 전에 append
        KFC(lev+1)
        path.pop()      # 함수 종료되고 pop

KFC(0)
'''


# 순열 코드
'''
path = []
used = [0] * 7

def KFC(lev):
    if lev == 3:        # 주사위 3개 던진다.
        print(*path)
        return

    for i in range(1, 7):   # 주사위 눈금이 1~6까지 (branch 6)
        if used[i] == 1:
            continue
        used[i] = 1
        path.append(i)
        KFC(lev+1)
        path.pop()
        used[i] = 0

KFC(0)
'''

"""
arr = ["A", "B", "C"]
n = len(arr)
# 0b110 (이진수) -> 6 (십진수)
def get_sub(tar):
    for i in range(n):
        # if tar & 1 -> 0x1 가독성 : 이 연산은 비트연산입니다.
        if tar & 0x1:   # 마지막 자리가 1인지 확인
            print(arr[i], end = " ")
        tar >>= 1 # 오른쪽으로 한번 민다.


for tar in range(1 << n):   # 2의 n제곱
    # 0부터 7까지 (000, 001, 010, 011, 100, 101, 110, 111)
    print("{", end = " ")
    get_sub(tar)
    print("}")
"""

"""
arr = ['A', 'B', 'C', 'D', 'E']
# 5명 중에 3명을 뽑는 조합
for a in range(5):
    start1 = a + 1
    for b in range(start1, 5):
        start2 = b + 1
        for c in range(start2, 5):
            print(arr[a], arr[b], arr[c])

# 5명 중에서 3명 뽑는다. -> 조합
# branch : 5 (최대 5), level : 3
"""

arr = ['A', 'B', 'C', 'D', 'E']
path = []

n = 3 # 5명 중에서 3명 뽑는다.

def KFC(lev, start):
    if lev == n:    # level은 3
        print(*path)
        return

    for i in range(start, 5):   # branch는 최대 5
        path.append(arr[i])
        KFC(lev+1, i+1)
        path.pop()

KFC(0, 0)