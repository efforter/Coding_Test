import sys
input = sys.stdin.readline

n = int(input())
game_max = list(map(int,input().split()))
game_min = game_max[:]

for _ in range(1,n):
    values = list(map(int,input().split()))

    max_0 = values[0] + max(game_max[0], game_max[1])
    max_1 = values[1] + max(game_max[0], game_max[1], game_max[2])
    max_2 = values[2] + max(game_max[1], game_max[2])

    min_0 = values[0] + min(game_min[0], game_min[1])
    min_1 = values[1] + min(game_min[0], game_min[1], game_min[2])
    min_2 = values[2] + min(game_min[1], game_min[2])

    game_max = [max_0,max_1,max_2]
    game_min = [min_0,min_1,min_2]

print(max(game_max),min(game_min))