ls = [1, 5, 2, 7, 3, 6]
print(*ls)
print(ls[0], ls[-1])
print(*ls[1::2])
print(*ls[::-1])

# answer
print()
arr = [1, 5, 2, 7, 3, 6]

print(*arr)
# print(arr[0], arr[-1])
print(arr[0], arr[len(arr) - 1])
print(*arr[1::2])
print(*arr[::-1])
