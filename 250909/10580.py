
import sys

sys.stdin = open("input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    target = []
    cnt = 0
    N = int(input())
    for _ in range(N):
        A, B = map(int, input().split())
        target.append((A, B))
    # target.sort(key=lambda x: x[1])
    for jeonbotdae1 in target:
        for jeonbotdae2 in target:
            if jeonbotdae1 == jeonbotdae2:
                continue
            if jeonbotdae2[0] > jeonbotdae1[0] and jeonbotdae2[1] < jeonbotdae1[1]:
                cnt += 1
            if jeonbotdae1[0] > jeonbotdae2[0] and jeonbotdae1[1] < jeonbotdae2[1]:
                cnt += 1

    result = cnt // 2
    print(f"#{tc} {result}")


'''
def get_result():
    size = len(arr)
    cnt = 0
    for i in range(size):
        for tar in range(i):
            i_a, i_b = arr[i][0], arr[i][1]
            tar_a, tar_b = arr[tar][0], arr[tar][1]

            if i_b < tar_b:
                cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for n in range(N):
        a, b = map(int, input().split())
        arr.append((a, b))

    arr.sort(key = lambda x:x[0])
    result = get_result()
    print(f"#{tc} {result}")
'''