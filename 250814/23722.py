# arr = list(input().split())
# n = len(arr)
# cnt = 0
# total = 0
#
# # 0b110 (이진수) -> 6 (십진수)
# def get_sub(tar):
#     global cnt
#     global total
#     for i in range(n):
#         # if tar & 1 -> 0x1 가독성 : 이 연산은 비트연산입니다.
#         if tar & 0x1:   # 마지막 자리가 1인지 확인
#             # print(arr[i], end = " ")
#             cnt += 1
#             if cnt == 2:
#                 total += 1
#
#         tar >>= 1 # 오른쪽으로 한번 민다.
#     cnt = 0
#
#
# for tar in range(1 << n):   # 2의 n제곱
#     # 0부터 7까지 (000, 001, 010, 011, 100, 101, 110, 111)
#     get_sub(tar)
# print(total)

'''
arr = list(input().split())
n = len(arr)

total = 0

def get_sub(target):
    cnt = 0
    global total

    for i in range(n):
        if target & 0x1:
            print(arr[i], end = " ")
            cnt += 1

        target >>= 1
    if cnt >= 2:
        total += 1


for target in range(1 << n):
    get_sub(target)
    print()

print(total)
'''

"""
arr = list(input().split())
n = len(arr)

total = 0


def get_sub(target):
    cnt = 0
    for i in range(n):
        if target & 0x1:
            cnt += 1

        target >>= 1
    return cnt


result = 0
for target in range(1 << n):
    if get_sub(target) >= 2:
        result += 1

print(result)
"""



