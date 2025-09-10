"""
def merge(left, right):
    global cnt
    result = [0] * (len(left) + len(right))
    l = r = 0

    if left[-1] > right[-1]:
        cnt += 1

    while l < len(left) and r < len(right):

        if left[l] < right[r]:
            result[l + r] = left[l]
            l += 1
        else:
            result[l + r] = right[r]
            r += 1

    while l < len(left):
        result[l + r] = left[l]
        l += 1

    while r < len(right):
        result[l + r] = right[r]
        r += 1

    return result


def merge_sort(lst):
    if len(lst) == 1:
        return lst

    center = len(lst) // 2
    left = lst[0:center]
    right = lst[center:]

    left_lst = merge_sort(left)
    right_lst = merge_sort(right)

    result = merge(left_lst, right_lst)
    return result


t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    result = merge_sort(lst)
    print(f"#{tc}", result[N // 2], cnt)
"""
cnt = 0

def merge_sort(arr):
    global cnt
    # 배열의 길이가 1이하면 이미 정렬이 끝났다
    if len(arr) <= 1:
        return arr
    # 배열을 반으로 나누기위한 인덱스
    mid = len(arr) // 2
    # 왼쪽 절반을 재귀적으로 정렬
    left = merge_sort(arr[:mid])
    # 오른쪽 절반을 재귀적으로 정렬
    right = merge_sort(arr[mid:])
    # 정렬된 왼쪽과 오른쪽 배열을 병합
    result = merge(left, right)

    return result

def merge(left, right):
    global cnt
    result = []
    i, j = 0, 0# i: 왼쪽, j: 오른쪽
    # 왼쪽과 오른쪽배열을 비교하면서 병합

    if left[-1] > right[-1]: cnt += 1

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            # 왼쪽 요소가 더 작으니까 result에 append
            result.append(left[i])
            i += 1 # element 이동(인덱스 이동)
        else:
            result.append(right[j])
            j += 1 # 그다음 element 이동
    # while문이 종료되면 남은것들 extend
    result.extend(left[i:])
    result.extend(right[j:])

    return result

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    sorted_arr = merge_sort(arr)
    print(f'#{tc} {sorted_arr[N//2]} {cnt}')