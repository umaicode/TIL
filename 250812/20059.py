t = int(input())

for tc in range(1, t + 1):
    formula = list(input().split())
    stack = []
    answer = "error"
    for ch in formula:
        if ch.isdigit():
            stack.append(int(ch))

        elif ch in "+-*/":
            if len(stack) < 2:
                answer = "error"
                break

            num1 = stack.pop()
            num2 = stack.pop()
            if ch == "+":
                stack.append(num2 + num1)
            elif ch == "-":
                stack.append(num2 - num1)
            elif ch == "*":
                stack.append(num2 * num1)
            elif ch == "/":
                if num1 == 0:
                    answer = "error"
                    break
                stack.append(num2 // num1)
        elif ch == ".":
            if len(stack) == 1:
                answer = stack.pop()
            break
        else:
            answer = "error"
            break

    print(f"#{tc} {answer}")
