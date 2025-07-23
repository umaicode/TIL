def reversed_num(number):
    str_num = str(number)
    reversed_num = int(str_num[::-1])
    return reversed_num


print(reversed_num(12345))

"""
num = 12345


# 함수 정의
def reverse_func(num):
    num = str(num)  # 재할당
    num = num[::-1]  # 거꾸로 슬라이싱
    return num


result = reverse_func(num)  # 함수 호출
print(result)
"""
