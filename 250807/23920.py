T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    players = list(map(int, input().split()))
    players.sort()

    new_players = []
    for i in range(n):
        for j in range(1, n):
            if abs(players[i] - players[j]) > k:
                new_players.append(players[i])
        new_players.append(players[i])
    print(new_players)
