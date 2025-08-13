t = int(input())

for tc in range(1, t + 1):
    str1 = input()
    str2 = input()

    result = 1

    if str1 in str2:
        result = 1
    else:
        result = 0

    print(f"#{tc} {result}")
