a = [[5, 5, 2, 6], [9, 1, 1, 3]]
tar = [5, 6, 1, 1, 1, 1, 5, 4]


def get_count():
    a_count = [[0] * 4 for _ in range(2)]
    for i in range(2):
        for j in range(4):
            for num in tar:
                if a[i][j] == num:
                    a_count[i][j] += 1

    return a_count


result = get_count()

for row in result:
    print(*row)
