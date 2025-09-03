def change(n):
    binary = ""
    power = -1  # 2의 -1제곱부터 시작
    cnt = 0

    while n > 0 and cnt < 13:
        value = 2 ** power  # 2의 -1 제곱, 2의 -2 제곱 ...

        if n >= value:  # 현재 자리값을 뺄 수 있다.
            binary += "1"  # 이진수 1
            n -= value  # 값 빼주고
        else:
            binary += "0"  # 자리값을 뺼 수 없으면 0

        power -= 1
        cnt += 1

    if n > 0:  # 계산이 끝났는데도 n이 남아있다면
        return "overflow"
    else:
        return binary


t = int(input())
for tc in range(1, t + 1):
    n = float(input())
    result = change(n)  # 함수 호출
    print(f'#{tc} {result}')
