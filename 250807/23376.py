def get_count(n):
    cnt = 0
    for num in a:
        if num == n:
            cnt += 1

    return cnt


a = [5, 2, 5, 7, 3]
n = int(input())

print(get_count(n))
