ls = [0] * 6

ls[0] = 2
ls[1] = 5
ls[2] = 1
ls[3] = 6
ls[4] = 4
ls[5] = 3

total = 0
max_v = 0
min_v = float("inf")

for nums in ls:
    total += nums
    if nums > max_v:
        max_v = nums
    if nums < min_v:
        min_v = nums

print(total)
print(max_v - min_v)
