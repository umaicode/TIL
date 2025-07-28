sum_num = 0
while True:
    n = int(input())
    if n > 0:
        sum_num += n
    elif n < 0:
        print(sum_num)
        sum_num = 0
    else:
        print(sum_num)
        break
