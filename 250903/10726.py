"""
t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())

    result = ""
    # if m & ((1 << n) - 1) == (1 << n) - 1:
    if (m + 1) % (1 << n) == 0:
        result = "ON"
    else:
        result = "OFF"

    print(f"#{tc} {result}")
"""

# 첫번쨰 방법
"""
t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    TOGGLE = "ON"
    for i in range(n):
        if m & (1 << i):
            continue
        TOGGLE = "OFF"
        break

    print(f"#{tc} {TOGGLE}")
"""


# 두번쨰 방법
def solve():
    tar = M
    for i in range(N):
        if tar & 0x1 == 0:
            return "OFF"

        tar >>= 1  # N번 반복하면서 오른쪽으로 한번씩 민다.
    return "ON"


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    print(f"#{tc} {solve()}")
