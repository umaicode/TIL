text = "helloworld[92084]answer"

start = text.find("9")
end = text.find("4")
for i in range(start, end + 1):
    print(text[i], end="")
