def is_even(arr):
    for i in arr:
        if i % 2 == 0:
            return True

    return False


arr = list(map(int, input().split()))

if is_even(arr):
    print(1)
else:
    print(0)
