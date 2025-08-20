path = []


# 중복 순열
def KFC(level):
    if level == 2:
        print(path)     # 정점 레벨에 도달했을 때
        return

    for i in range(3):  # 0, 1, 2 branch : 3
        path.append(i)
        KFC(level + 1)
        path.pop()


KFC(0)


# 순열 (중복순열에 used 배열)
# 주사위 3개를 던져 나올 수 있는 순열

path = []
used = [0] * 7


def KFC2(level):
    if level == 3:
        print(path)
        return

    for i in range(1, 7):
        if used[i]:
            continue
        used[i] = 1  # used 배열에 기록
        path.append(i)
        KFC2(level + 1)
        path.pop()
        used[i] = 0  # used 배열에 기록 지우기


KFC2(0)


# 부분집합은 항상 branch : 2인 중복순열 ('O', 'X')
# 5명으로 이루어진 부분집합 : level : 5

arr = ["O", "X"]
path = []
name = ["A", "B", "C", "D", "E"]


def print_name():
    for i in range(5):
        if path[i] == "O":
            print(name[i], end=" ")
    print()


def KFC3(level):
    if level == 5:
        print_name()
        return

    for i in range(2):  # branch : 2
        path.append(arr[i])
        KFC3(level + 1)
        path.pop()


KFC3(0)


# 조합
# a b c 와 b a c는 같은 조합
# 핵심 : 앞에서 뽑았던 경우의 수를 제외하고 시작(start 매개변수 추가)
# 5명 중에 3명 뽑는다
# level : 3, branch : 최대 5

arr = ["A", "B", "C", "D", "E"]
path = []


def KFC4(level, start):
    if level == 3:
        print(path)
        return

    for i in range(start, 5):  # branch : 최대 5
        path.append(arr[i])
        KFC4(level + 1, i + 1)
        path.pop()


KFC4(0, 3)


# 다툰친구 B와 T
# 중복순열 + 가지치기 ---> 완전탐색 유형 문제 (백트래킹 문제)
