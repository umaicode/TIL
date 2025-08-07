criminals = [[5, 7, 9, 55], [30, 10, 6, 8]]
residents = [[1, 2, 3, 4], [5, 7, 10, 15]]

dat = [0] * 56

residents_count = 0
criminals_count = 0

for i in range(2):
    for j in range(4):
        dat[criminals[i][j]] += 1
        dat[residents[i][j]] += 2


for i in range(len(dat)):
    if dat[i] == 2:
        residents_count += 1
    for row in residents:
        if dat[i] == 3 and dat[i] in row:
            criminals_count += 1

print(criminals_count, residents_count)
