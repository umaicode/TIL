n = int(input())
blocks = list(map(int, input().split()))

blocks.sort()
total = 100
cnt = 0
for block in blocks:
    total -= block
    if total < 0:
        break
    cnt += 1

print(cnt)
