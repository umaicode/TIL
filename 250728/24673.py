arr = []
while True:
    n = int(input())
    if n == 0:
        for i in range(len(arr)):
            print(arr.pop(), end="")
        break
    else:
        arr.append(n)
