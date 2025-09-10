def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    direction = 0
    while start <= end:  # start와 end가 같아질때까지
        mid = (start + end) // 2
        # 이진 탐색을 통해서 타겟을 찾으면 middle 인덱스 반환
        if arr[mid] == target:
            return True
        # 타겟이 중간값 보다 크면 오른쪽 부분 탐색
        elif arr[mid] < target:
            if direction == 2:
                return False
            direction = 2
            start = mid + 1
        else:  # 타겟이 중간값보다 작으면 왼쪽 부분 탐색
            if direction == 1:
                return False
            direction = 1
            end = mid - 1
    # 타겟 못찾으면
    return False


t = int(input())

for tc in range(1, t + 1):
    cnt = 0
    n, m = map(int, input().split())
    lst_a = list(map(int, input().split()))
    lst_b = list(map(int, input().split()))

    lst_a.sort()
    for num in lst_b:
        if binary_search(lst_a, num):
            cnt += 1

    print(f"#{tc} {cnt}")
