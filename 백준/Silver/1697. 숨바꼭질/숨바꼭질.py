import sys
input = sys.stdin.readline
from collections import deque

def BFS(n,k):
    q = deque([n])
    while q:
        s = q.popleft()
        if s==k:
            print(visited[s])
            break
        for x in (s-1,s+1,s*2):
            if 0 <= x <= MAX and not visited[x]:
                visited[x] = visited[s] + 1
                q.append(x)
                
n,k = map(int,input().split())
MAX = 10**5
visited = [0] * (MAX+1)
BFS(n,k)