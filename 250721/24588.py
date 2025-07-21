char = "Hello World"
print(char[0] + " " + char[10])
for i in range(len(char)):
    if i % 2 == 0:
        print(char[i], end="")
print()
print(char[::-1])


# length = len(char)
# print(length)
# print(char[::2])
# print(char[::-1])
