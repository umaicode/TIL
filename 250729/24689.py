# numbers = list(map(int, input().split()))


# def valid_numbers(numbers):
#     lottery = set()
#     for number in numbers:
#         lottery.add(number)
#     if len(lottery) != 6:
#         return "INVALID"
#     for num in lottery:
#         if num < 1 or num > 45:
#             return "INVALID"
#     return "VALID"


# print(valid_numbers(numbers))


numbers = list(map(int, input().split()))

# lotto = {}    # 딕셔너리
lotto = set()
for num in numbers:
    if 1 <= num <= 45:  # 2번 조건
        lotto.add(num)
if len(lotto) == 6:  # 1번 조건
    print("VALID")
else:
    print("INVALID")
