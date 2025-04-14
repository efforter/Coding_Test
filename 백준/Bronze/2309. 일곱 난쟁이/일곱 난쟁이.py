import sys
input = sys.stdin.readline

ary=[]
for _ in range(9):
    ary.append((int(input())))

ary.sort()
temp = sum(ary)

for i in range(9):
    for j in range(i+1,9):
        if ary[i]+ary[j]==temp-100:
            a = ary[i]
            b = ary[j]
            ary.remove(a)
            ary.remove(b)
            break
    if len(ary)==7:
        break

for s in range(len(ary)):
    print(ary[s])