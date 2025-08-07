a, b = map(int, input().split())

matrix = [[1, 2, 1, 3, 1], [2, 2, 2, 2, 2], [1, 0, 1, 0, 1], [3, 1, 2, 1, 3]]

dx = [0, -1, 1, 1]
dy = [1, 0, 0, 1]

numbers = []

for i in range(4):
    if 0 <= a + dy[i] < 4 and 0 <= b + dx[i] < 5:
        numbers.append(matrix[a + dy[i]][b + dx[i]])
    else:
        continue


# print(numbers)
print(max(numbers))
