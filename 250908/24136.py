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
