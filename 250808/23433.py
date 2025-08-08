text = ["GOLDABCGOLD", "HELLOWORLD", "WHITEGOLD"]
total = 0


def find_gold(text):
    cnt = 0
    start = 0
    while True:
        start = text.find("GOLD", start)
        if start == -1:
            break
        cnt += 1
        start += 1
    return cnt


for string in text:
    total += find_gold(string)

print(total)
