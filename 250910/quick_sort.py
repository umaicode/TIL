def quick_sort(arr):
    # 정복 : 배열의 길이가 1이하면 return
    if len(arr) <= 1: return arr

    # 피벗을 배열의 중간 요소로 선택
    pivot = arr[len(arr) // 2]
    # 피벗보다 작은 요소들은 left 리스트에 담음
    left = [x for x in arr if x < pivot]
    # 피벗과 같은 요소들은 middle 리스트에 담음
    middle = [x for x in arr if x == pivot]
    # 피벗보다 큰 요소들은 right 리스트에 담음
    right = [x for x in arr if x > pivot]

    # 재귀 호출
    result = quick_sort(left) + middle + quick_sort(right)

    return result

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(arr)
print(*sorted_arr)