text = "ABCDEFABCKKKKKABC"
cnt = 0
start = 0

while True:
    start = text.find("ABC", start)
    if start == -1:
        break
    cnt += 1
    start += 1

print(cnt)
