N = int(input())
numbers = list(map(int, input().split()))
if len(numbers) == N:
    numbers.sort()
    for number in numbers:
        print(number, end="")
else:
    exit()
