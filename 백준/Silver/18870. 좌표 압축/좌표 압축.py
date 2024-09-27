import sys
input = sys.stdin.readline

n = int(input())
X = list(map(int,input().split()))
X1 = []
for i,x in enumerate(X):
    X1.append([x,i])

X2 = sorted(X1)

result = [0 for _ in range(n)]
temp = 0
for i in range(n):
    if i ==0:
        temp+=1
        continue
    else:
        if X2[i-1][0] == X2[i][0]:
            result[i] = result[i-1]
        else:
            result[i] = temp
            temp+=1

for i in range(n):
    X2[i][0] = result[i]

X2.sort(key=lambda x:x[1])
for i in X2:
    print(i[0],end=' ')