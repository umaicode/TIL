def count_num(number):
    str_num = str(number)
    num_list = list(map(int, str_num))
    even = list(map(lambda x: x % 2 == 0, num_list))
    even_count = even.count(True)
    odd_count = even.count(False)
    # print(sum(even))

    return even_count, odd_count


print(count_num(827364)[0])
print(count_num(827364)[1])


"""
# 전략 1번
num = str(num)
digit1 = int(num[0])    # 100만
digit2 = int(num[1])    # 10만

# 전략 2번 : 산술 연산자 //, %
digit1 = num // 1000000         # 100만
digit2 = (num // 100000) % 10   # 10만

# 전략 3번 : 짝수의 특징 : 2로 나눈 나머지가 0 : 판별식
print((digit1 % 2 == 0) + (digit2 % 2 == 0))    # 암시적 형변환 -> 1 + 1 = 2
"""

"""
num = 827364


def get_count(num):
    digit1 = num // 100000          # 10만의 자리
    digit2 = (num // 10000) % 10
    digit3 = (num // 1000) $ 10
    digit4 = (num // 100) % 10
    digit5 = (num // 10) % 10
    digit6 = num % 10               # 1의 자리

    even_cnt = (digit1 % 2 == 0) + (digit2 % 2 == 0) + (digit3 % 2 == 0) + (digit4 % 2 == 0) + (digit5 % 2 == 0) + (digit6 % 2 == 0)
    odd_cnt = 6 - even_cnt

    return even_cnt, odd_cnt

even_cnt, odd_cnt = get_count(num)
print(even_cnt)
print(odd_cnt)
"""
