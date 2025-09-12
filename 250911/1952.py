import sys

sys.stdin = open("input.txt", "r")

t = int(input())

def swimming(month, pay):
    global min_v
    if month >= 12:
        min_v = min(min_v, pay)
        return min_v

    if plan[month] != 0:
        # 1 일권
        swimming(month + 1, pay + tickets[0] * plan[month])
        # 1 달권
        swimming(month + 1, pay + tickets[1])
        # 3 달권
        swimming(month + 3, pay + tickets[2])
        # 1 년권
        swimming(month + 12, pay + tickets[3])
    else:
        swimming(month + 1, pay)


for tc in range(1, t + 1):
    # 0 : 1일
    # 1 : 1달
    # 2 : 3달
    # 3 : 1년
    min_v = float("inf")
    tickets = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    swimming(0, 0)

    print(f"#{tc} {min_v}")
