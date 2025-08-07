matrix = [[0] * 4 for _ in range(3)]

matrix[0][0] = 5
matrix[0][1] = 4
matrix[0][2] = 2
matrix[0][3] = 1

matrix[1][0] = 3
matrix[1][1] = 7
matrix[1][2] = 7
matrix[1][3] = 7

matrix[2][0] = 2
matrix[2][1] = 2
matrix[2][2] = 1
matrix[2][3] = 1

for y in range(4):
    for x in range(3):
        print(matrix[x][y], end=" ")
    print()
