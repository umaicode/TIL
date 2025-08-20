# from collections import deque

# t = int(input())

# for tc in range(1, t + 1):
#     n, m = map(int, input().split())

#     pizzas = list(map(int, input().split()))

#     pizza = []
#     for idx, value in enumerate(pizzas):
#         pizza.append([idx, value])

#     oven = deque()
#     for i in range(n):
#         oven.append(pizza.pop(0))

#     while True:
#         if len(oven) == 1:
#             last = oven.popleft()
#             result = last[0] + 1
#             break

#         temp = oven.popleft()
#         temp[1] = temp[1] // 2
#         if temp[1] == 0:
#             if len(pizza) != 0:
#                 oven.append(pizza.pop(0))
#             if len(pizza) == 0:
#                 continue
#         if temp[1] != 0:
#             oven.append(temp)

#     print(f"#{tc} {result}")

from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N : 화덕 크기, M : 피자 개수
    cheese = list(map(int, input().split()))

    # 인덱스 1부터 시작(+1), 치즈양
    pizzas = deque([[i + 1, p] for i, p in enumerate(cheese)])

    oven = deque()  # 화덕
    for _ in range(N):
        if pizzas:
            oven.append(pizzas.popleft())

    while len(oven) > 1:
        now = oven.popleft()  # 화덕에서 피자하나 꺼냄
        # now = [피자인덱스, 치즈의 양]
        now[1] //= 2  # 꺼낸 피자의 치즈 양을 절반으로 줄이고
        if now[1] == 0:  # 치즈가 모두 녹았다면
            if pizzas:  # 남은 피자가 있으면
                oven.append(pizzas.popleft())  # 새 피자 넣기
        else:  # 치즈가 아직 남아있다면 다시 화덕에 넣기
            oven.append(now)

    # while문 종료 후 피자 한개만 남아있음. 피자의 번호 출력
    # [피자인덱스, 치즈의양]
    print(f"#{tc} {oven[0][0]}")
