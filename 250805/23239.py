matrix = [list(map(int, input().split())) for _ in range(4)]
new_matrix = []
for i in range(3, -1, -1):
    new_matrix.append(sorted(matrix[i], reverse=True))

for i in range(4):
    print(*new_matrix[i])
