# 함수의 특징
# 1. 값만 복사된다.
# 2. 함수가 끝나면 함수를 호출했던 곳으로 돌아온다.
"""
def KFC(x):
    print(x)  ## 8
    x += 1
    BTS(x + 5)
    print(x)  ## 9


def BTS(x):
    print(x)  ## 14


x = 3
KFC(x + 5)
print(x)  ## 3
"""


def KFC(x):
    if x == 2:
        return
    KFC(x + 1)
    KFC(x + 1)
    print(x)


KFC(0)
