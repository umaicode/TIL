def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end: # start와 end가 같아질때까지
        mid = (start + end) // 2
        # 이진 탐색을 통해서 타겟을 찾으면 middle 인덱스 반환
        if arr[mid] == target:
            return mid
        # 타겟이 중간값 보다 크면 오른쪽 부분 탐색
        elif arr[mid] < target:
            start = mid + 1
        else: # 타겟이 중간값보다 작으면 왼쪽 부분 탐색
            end = mid - 1
    # 타겟 못찾으면
    return -1

arr = [1, 3, 5, 7, 9, 11 ,13, 15, 17]
target = 11
result = binary_search(arr, target)
print(f'target index : {result}')
