arr = ["A", "B", "Q", "T"]

for i in range(len(arr)):
    for j in range(len(arr) - 1, -1, -1):
        print(arr[j], end="")
    print()
