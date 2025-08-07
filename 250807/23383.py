arr = [[1, 5, 10, 15], [15, 15, 20, 30]]

dat = [0] * 31

for i in range(2):
    for j in range(4):
        dat[arr[i][j]] += 1

n = int(input())

for row in arr:
    for num in row:
        if num == n:
            print(dat[num])

print(dat)
