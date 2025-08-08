text = input()

start = 0
result = 0

for ch in text:
    if ch == "[":
        start = text.find("[", start)
        end = text.find("]", start)
        num = int(text[start + 1 : end])
        result += num
        start = end + 1

    if ch == "{":
        start = text.find("{", start)
        end = text.find("}", start)
        num = int(text[start + 1 : end])
        result *= num
        start = end + 1

print(result)
