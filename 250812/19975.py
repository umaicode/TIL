t = int(input())

for tc in range(1, t + 1):
    stack = []
    string = input()
    for ch in string:
        if stack:
            if stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        else:
            stack.append(ch)
    print(f"#{tc} {len(stack)}")
