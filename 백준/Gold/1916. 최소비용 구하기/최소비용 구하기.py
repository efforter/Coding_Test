import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, v = map(int, input().split())
    graph[s].append((e, v))

start, end = map(int, input().split())

def dijkstra(start):
    distance = [INF] * (N + 1)
    distance[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        if distance[current_node] < current_dist:
            continue
        
        for next_node, weight in graph[current_node]:
            cost = current_dist + weight
            
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(pq, (cost, next_node))
    
    return distance

distances = dijkstra(start)
print(distances[end])