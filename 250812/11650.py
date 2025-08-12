n = int(input())

coordinates = [tuple(map(int, input().split())) for _ in range(n)]

coordinates.sort(key=lambda x: (x[0], x[1]))

for coordinate in coordinates:
    print(*coordinate)
