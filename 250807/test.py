"""
부분집합

재귀호출 ---> 백트래킹 ---> 순열, 조합, 부분집합

부분집합은 반드시 재귀로만 가능한가???
부분집합은 비트연산으로 가능!!

이진탐색

선택정렬
"""

"""
# flag 처리 : flag 변수를 bool 타입 변수로 활용
# for - break ---> break를 함수의 return으로 바꾼다.
# Q) arr1과 arr2가 같은지 판별하세요

arr1 = [1, 4, 2, 5]
arr2 = [1, 4, 3, 5]

for i in range(4):
    if arr1[i] != arr2[2]:  # 하나라도 같지 않으면
        flag = 1
        break

if flag:
    print("x")
else:
    print("o")
"""

"""
arr1 = [1, 4, 2, 5]
arr2 = [1, 4, 3, 5]


def is_same():
    for i in range(4):
        if arr1[i] != arr2[i]:
            return 1  # 하나라도 같지 않으면 return 1

    return 0  # 모두 같으면 return 0


result = is_same()
if result:
    print("x")
else:
    print("o")
"""

"""
A = [[5, 5, 2, 6], [9, 1, 1, 3]]
tar = [5, 6, 1, 1, 1, 1, 5, 4]


def get_count(n):
    cnt = 0
    for i in range(len(tar)):
        if tar[i] == n:
            cnt += 1
    return cnt


for y in range(2):
    for x in range(4):
        result = get_count(A[y][x])
        print(result, end=" ")
    print()
"""
