money = int(input())

moneys = [500, 100, 50, 10]

total = 0
cnt = 0

for num in moneys:
    total = money // num
    money %= num * total
    cnt += total

print(cnt)
