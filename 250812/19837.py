t = int(input())

for tc in range(1, t + 1):
    string = input()
    stack = []
    result = 1

    for ch in string:
        if ch == "(":
            stack.append(")")
        elif ch == "{":
            stack.append("}")

        elif ch == ")" or ch == "}":
            if not stack or stack.pop() != ch:
                result = 0
                break

        if stack:
            result = 0
        else:
            result = 1

    print(f"#{tc} {result}")
