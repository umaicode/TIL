arr = [0] * 5


for idx, value in enumerate(arr):
    arr[idx] = idx + 5

print(*arr)
