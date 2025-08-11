n = int(input())

times = []

for _ in range(n):
    start, end = map(int, input().split())
    times.append((start, end))

result = []
cnt = 0
dat = [0] * 11
times.sort(key=lambda x: x[1])
for time in times:
    if time[1] < 4:

# print(result)
