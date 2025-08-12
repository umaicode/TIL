t = int(input())

for tc in range(1, t + 1):
    pay = int(input())
    moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = []
    string = ""
    cnt = 0
    for money in moneys:
        cnt = pay // money
        pay -= money * cnt
        result.append(cnt)

    print(f"#{tc}")
    print(*result)
