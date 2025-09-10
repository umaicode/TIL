def merge_sort(arr):
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
    result = []
    i, j = 0, 0# i: 왼쪽, j: 오른쪽
    # 왼쪽과 오른쪽배열을 비교하면서 병합
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

# 예시 하드 코딩
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr)
print(*sorted_arr)
