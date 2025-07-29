numbers = list(map(int, input().split()))


def valid_numbers(numbers):
    lottery = set()
    for number in numbers:
        lottery.add(number)
    if len(lottery) != 6:
        return "INVALID"
    for num in lottery:
        if num < 1 or num > 45:
            return "INVALID"
    return "VALID"


print(valid_numbers(numbers))
