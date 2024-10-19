import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

cor = 'IOI' + (n-1) * 'OI'
result = 0

for i in range(m-(n*2)):
    temp = ''
    for j in range(i,i+n*2+1):
        temp += s[j]
    if temp == cor:
        result+=1
print(result)