arr = [[] for _ in range(3)]
arr[0] = ["A", "B", "T"]
arr[1] = []
arr[2] = ["R", "S"]

for i in range(3):
    arr[i].reverse()
    print("".join(arr[i]))
