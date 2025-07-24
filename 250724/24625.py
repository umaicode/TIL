arr = list(map(int, input().split()))

max_value = max(arr)
for idx, value in enumerate(arr):
    if value == max_value:
        print(idx)
        break
