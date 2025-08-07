text = "BBQBHCBTS"

dat = [0] * 91

for ch in text:
    dat[ord(ch)] += 1

print(max(dat))
