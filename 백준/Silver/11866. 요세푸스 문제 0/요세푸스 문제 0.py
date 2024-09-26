import sys
input = sys.stdin.readline

n,k = map(int,input().split())
circle = list(range(1,n+1))
temp = 0
result = []
for i in range(n):
    temp += k-1
    temp = temp%len(circle)
    result.append(circle[temp])
    circle.pop(temp)

print(f"<{', '.join(map(str,result))}>")