text = "ABCDE"
dat = [0] * 91

for ch in text:
    dat[ord(ch)] += 1

# print(dat)

string = input().split()

for ch in string:
    if dat[ord(ch)]:
        print("O", end=" ")
    else:
        print("X", end=" ")
