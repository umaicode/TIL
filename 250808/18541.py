T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    sample = input()
    passcode = input()
    sample = sample.replace(" ", "")
    passcode = passcode.replace(" ", "")
    start = 0
    flag = 1

    for ch in passcode:
        start = sample.find(ch, start)
        if start == -1:
            flag = 0
            break
        start += 1

    print(f"#{test_case} {flag}")
