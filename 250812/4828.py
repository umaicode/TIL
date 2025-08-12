t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    result = max(numbers) - min(numbers)
    print(f"#{tc} {result}")
