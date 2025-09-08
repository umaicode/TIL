lst = list(map(int, input().split()))
results = []
path = []
used = [0] * 6


def perm(level):
    if level == 6:
        results.append(path[:])
        return results

    for i in range(6):
        if used[i] == 1:
            continue
        used[i] = 1
        path.append(lst[i])
        perm(level + 1)
        path.pop()
        used[i] = 0


def is_baby_gin(results):
    is_answer = False

    def is_check(part):
        part.sort()
        if part[0] == part[1] == part[2]:
            return True
        if part[2] == part[1] + 1 and part[1] == part[0] + 1:
            return True

        return False

    for path in results:
        front = path[0:3]
        end = path[3:6]
        if is_check(front) and is_check(end):
            is_answer = True
            break

    return is_answer


perm(0)

if is_baby_gin(results):
    print("Yes")
else:
    print("No")


"""
used = [0] * 6
path = []
is_babygin = 0

def is_baby_gin():
    cnt = 0
    # 앞에 세자리가 triplet 또는 run
    a, b, c = path[0], path[1], path[2]
    if a == b == c: cnt += 1
    elif (a) == (b - 1) == (c - 2) : cnt += 1

    # 뒤에 세자리가 triplet 또는 run
    a, b, c = path[3], path[4], path[5]
    if a == b == c: cnt += 1
    elif (a) == (b - 1) == (c - 2) : cnt += 1

    return cnt == 2 # cnt 가 2면 baby-gin이 맞다!

# 순열 코드
def recur(lev):
    global is_babygin
    if lev == 6: # level은 6
        if is_baby_gin():
            is_babygin = 1
        return

    for i in range(6): # branch는 6
        if used[i] == 1: continue
        used[i] = 1
        path.append(arr[i])
        recur(lev + 1)
        path.pop()
        used[i] = 0

arr = list(map(int, input().split()))
recur(0)

if is_babygin: print('Yes')
else: print('No')

"""
