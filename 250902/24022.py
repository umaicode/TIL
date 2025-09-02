name = "BTAR"
MAP = [[0, 0, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0]]

n = int(input())

for i in range(4):
    # if MAP[n][i] == 1:
    #     print(name[i])
    # 단점 : 들여쓰기가 생긴다.
    if MAP[n][i] == 0:
        continue
    print(name[i])
