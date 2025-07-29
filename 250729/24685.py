n = int(input())
numbers = list(map(int, input().split()))
num_set = set()
ordered_numbers = []
idx = int(input())

for num in numbers:
    if num not in num_set:
        num_set.add(num)
        ordered_numbers.append(num)


print(len(num_set))
for num in ordered_numbers:
    print(num, end=" ")
print()
print(ordered_numbers[idx - 1])
