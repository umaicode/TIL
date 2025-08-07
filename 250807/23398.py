T = int(input())

for test_case in range(1, T + 1):
    answer = ""
    routes = int(input())
    route = []
    stop = []
    for i in range(routes):
        route.append(tuple(map(int, input().split())))
    number = int(input())
    for i in range(number):
        stop.append(int(input()))

    dat = [0] * 5001
    # print(route)

    for start, end in route:
        for i in range(start, end + 1):
            dat[i] += 1

    for num in stop:
        answer += str(dat[num]) + " "

    print(f"#{test_case} {answer.strip()}")
