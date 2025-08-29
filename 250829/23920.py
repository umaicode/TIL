# def baseball(arr, k):
#     arr.sort()
#     left, right = 0, 0
#     max_cnt = 0
#     cnt = 0
#     while True:

#         if right == n:
#             break
#         if arr[right] - arr[left] <= k:
#             right += 1
#             cnt += 1
#         else:
#             # arr[right] - arr[left] > k:
#             left += 1
#             cnt -= 1

#         max_cnt = max(max_cnt, cnt)
#     return max_cnt


# t = int(input())

# for tc in range(1, t + 1):
#     n, k = map(int, input().split())
#     arr = list(map(int, input().split()))
#     result = baseball(arr, k)
#     print(f"#{tc} {result}")


T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    players = list(map(int, input().split()))

    players.sort()  # 오름차순 정렬

    left, right = 0, 0
    ret = 0

    while left < n and right < n:
        # 실력차이가 k 초과
        if players[right] - players[left] > k:
            left += 1  # 범위 넓히기

        # 실력차이가 k 이하
        else:
            right += 1  # 범위 좁히기

        # right - left + 1
        # right가 +1 되고 크기를 계산
        # right - left 로 끝내야 한다.
        ret = max(right - left, ret)
    print(f"#{tc} {ret}")
