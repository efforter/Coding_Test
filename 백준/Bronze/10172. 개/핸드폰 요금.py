import sys
input = sys.stdin.readline

n = int(input())
ary = list(map(int,input().split()))
y = m = 0
for x in ary:
    y += ((x//30)+1)*10
    m += ((x//60)+1)*15

if y > m:
    print(f"M {m}")

elif y==m:
    print(f"Y M",y)

else:
    print(f"Y {y}")
