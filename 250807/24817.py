height, width = map(int, input().split())

apart = [list(map(int, input().split())) for _ in range(height)]

bheight, bwidth = map(int, input().split())

blacklist = [list(map(int, input().split())) for _ in range(bheight)]

dat = [0] * 100001

criminal = 0
people = 0

for i in range(bheight):
    for j in range(bwidth):
        dat[blacklist[i][j]] = 1


for i in range(height):
    for j in range(width):
        if dat[apart[i][j]] == 1:
            criminal += 1
        else:
            people += 1

print(criminal)
print(people)
