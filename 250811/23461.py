from itertools import permutations

times = list(map(int, input().split()))

times = list(permutations(times))

result = []

for time in times:
    sum_v = 0
    for i in range(len(time)):
        sum_v += time[i] * (len(time) - 1 - i)
    result.append(sum_v)

print(min(result))
