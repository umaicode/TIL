"""
cnt 변수는 global로 해야하는 이유는 scope
-> factorial에서 사용하기 위해서 외부에 있는 cnt를 가져와야 하기 때문
-> global 없이는 사용 불가
"""

cnt = 0


def factorial(n):
    # cnt = 0   # 문제점 : 재귀호출 할때마다 0으로 초기화
    global cnt  # 전역변수 cnt를 수정
    cnt += 1
    # 기저 조건
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)  # 재귀 호출


factorial(5)
print(cnt)
