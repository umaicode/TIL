matrix = [list(map(int, input().split())) for _ in range(5)]

cnt = 0
max_v = float("-inf")
min_v = float("inf")
total = 0

for list in matrix:
    for num in list:
        if num == 2:
            cnt += 1
        if num >= max_v:
            max_v = num
        if num <= min_v:
            min_v = num


for i in range(5):
    total += matrix[i][i]

print(cnt)
print(max_v, min_v)
print(total)
