N = int(input())
friends = [1, 2, 3]
for i in range(N):
    friends.append(friends.pop(0))

print(friends[0])
