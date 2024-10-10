from itertools import combinations
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
house = []
chicken = []

for i in range(n):
    temp = list(map(int,input().split()))

    for j in range(n):
        if temp[j]==1:
            house.append((i,j))
        elif temp[j]==2:
            chicken.append((i,j))

map = [[] for _ in range(len(chicken))]
for i in range(len(chicken)):
    for j in range(len(house)):
       map[i].append(abs(chicken[i][0]-house[j][0])+abs(chicken[i][1]-house[j][1]))

min_chicken = float('inf')

for comb in combinations(map, m):
    total_distance = 0
    for h in range(len(house)):
        min_distance = float('inf')
        for dist in comb:
            min_distance = min(min_distance, dist[h])
        total_distance += min_distance
    
    min_chicken = min(min_chicken, total_distance)

print(min_chicken)