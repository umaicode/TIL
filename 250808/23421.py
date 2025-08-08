string = input()


def is_pelindrome(string):
    for i in range(len(string) // 2):
        if string[i] == string[len(string) - 1 - i]:
            continue
        else:
            return 0

    return 1


print(is_pelindrome(string))
